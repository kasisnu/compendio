# USAGE
# python classify.py --model models/svm.cpickle --image images/umbc_zipcode.png

# import the necessary packages
from pyimagesearch.hog import HOG
from pyimagesearch import dataset
from pyimagesearch import imutils
import argparse
import cPickle
import mahotas
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required = True,
	help = "path to where the model will be stored")
ap.add_argument("-i", "--image", required = True,
	help = "path to the image file")
args = vars(ap.parse_args())

# load the model
model = open(args["model"]).read()
model = cPickle.loads(model)

# initialize the HOG descriptor
hog = HOG(orientations = 18, pixelsPerCell = (10, 10),
	cellsPerBlock = (1, 1), normalize = True)

# load the image and convert it to grayscale
image = cv2.imread(args["image"])

# Resize image to 1000 x 1000
if image.shape[1] > 1000:
	image = imutils.resize(image, width = 1000)
elif image.shape[0] > 1000:
	image = imutils.resize(image, height = 1000)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# crop the leftmost 15% of columns, since they are the most likely to contain 
# the handwritten digits

cropped = gray[:,0:int(0.15*gray.shape[1])]
# cv2.imshow("cropped", cropped)

edged = cv2.Canny(cropped, 30, 150)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# sort the contours by their x-axis position, ensuring
# that we read the numbers from left to right
cnts = sorted([(c, cv2.boundingRect(c)[1]) for c in cnts], key = lambda x: x[1])

# loop over the contours
for (c, _) in cnts:
	# compute the bounding box for the rectangle
	(x, y, w, h) = cv2.boundingRect(c)

	# if the width is at least 4 pixels and the height
	# is at least 20 pixels, the contour is likely a digit
	if w >= 4 and h >= 20:
		# crop the ROI and then threshold the grayscale
		# ROI to reveal the digit
		roi = gray[y:y + h, x:x + w]
		thresh = roi.copy()
		T = mahotas.thresholding.otsu(roi)
		thresh[thresh > T] = 255
		thresh = cv2.bitwise_not(thresh)

		# deskew the image center its extent
		thresh = dataset.deskew(thresh, 20)
		thresh = dataset.center_extent(thresh, (20, 20))

		# extract features from the image and classify it
		hist = hog.describe(thresh)
		digit = model.predict(hist)[0]
		print "I think that number is: %d" % (digit)

		# draw a rectangle around the digit, the show what the
		# digit was classified as
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
		cv2.putText(image, str(digit), (x - 20, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
		cv2.imshow("image", image)

cv2.waitKey(0)