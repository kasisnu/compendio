# USAGE
# python final.py --model models/svm.pickle --image <path to image>

from imtotext import OCR
from classifier import EYE
from itertools import izip
from pyimagesearch import imutils
import cv2
import argparse


def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

def main():
	
	# parse command line arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-m","--model",required = True,
		help = "Path to the model pickle file")
	ap.add_argument("-i","--image",required = True,
		help = "Path to the image file")
	args = vars(ap.parse_args())

	# initialize the classifier
	eye = EYE(args["model"])

	image = args["image"]

	# load the image and convert it to grayscale
	image = cv2.imread(image)

	# Resize image to 1000 x 1000
	if image.shape[1] > 1000:
		image = imutils.resize(image, width = 1000)
	elif image.shape[0] > 1000:
		image = imutils.resize(image, height = 1000)

	cv2.imshow("Original",image)

	# get list of tuples(<digit>,<contour>) from digit classifier
	markers = eye.getMarkers(image)

	# check if markers are valid
	markersValid = True
	print "Marker pairs:"
	for pair in pairwise(markers):
		# the second digit must be 0, to define the end of a bullet point
		print "%d, %d" % (pair[0][0],pair[1][0])
		#if pair[1][0] != 0:
		#	markersValid = False
		#	break

	if not markersValid:
		print "Markers are not valid. The script will now exit."

	else:
		for startMarker,stopMarker in pairwise(markers):
			(x1, y1, w1, h1) = cv2.boundingRect(startMarker[1])
			(x2, y2, w2, h2) = cv2.boundingRect(stopMarker[1])

			cropped = image[y1-(h1/2):y2+h2,x1+(w1+w2)/2:]
			cv2.imshow(str(startMarker[0]),cropped)
		cv2.waitKey(0)
if __name__ == '__main__':
  main()
