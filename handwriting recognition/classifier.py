# USAGE
# python classify.py --model models/svm.cpickle --image images/umbc_zipcode.png

# import the necessary packages
from pyimagesearch.hog import HOG
from pyimagesearch import dataset
from pyimagesearch import imutils
import cPickle
import mahotas
import cv2

class EYE:
	def __init__(self, model):
		# load the model
		self.model = open(model).read()
		self.model = cPickle.loads(self.model)

		# initialize the HOG descriptor
		self.hog = HOG(orientations = 18, pixelsPerCell = (10, 10),
			cellsPerBlock = (1, 1), normalize = True)

	def getMarkers(self, image):
		" Returns a list of tuples(<digit>,<contour>). "
		
		markers = []

		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		# crop the leftmost 15% of columns, since they are the most likely to contain 
		# the handwritten digits

		cropped = gray[:,0:int(0.15*gray.shape[1])]

		edged = cv2.Canny(cropped, 30, 150)
		(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		# sort the contours by their y-axis position, ensuring
		# that we read the numbers from top to bottom
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
				hist = self.hog.describe(thresh)
				digit = self.model.predict(hist)[0]
				markers.append((digit,c))

		return markers