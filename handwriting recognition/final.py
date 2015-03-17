# USAGE
# python final.py --model models/svm.cpickle --image images/deskew_marked_text.jpg

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

def stripText(text):
	''' Removes all characters until a period is encountered,
		if the first character in the string is lowercase. Also removes 
		all characters from the tail until a period is encountered.
	'''
	i = 0
	if text[0].islower() or not text[0].isalpha():
		while text[i] != '.':
			i += 1
		i += 1

	j = len(text) - 1
	if text[j].islower() or not text[j].isalpha():
		while text[j] != '.':
			j -= 1

	stripped = text[i:j+1]
	return stripped


def listToText(results):
	# sort result on the basis of digits
	results = sorted(results, key = lambda x: x[0])
	s = ""
	for digit,text in results:
		s += str(digit)
		s += ') '
		s += text
		s += '\n\n'
	return s

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
		# Initialize OCR, and store the results in a list. 
		ocr = OCR()
		results = []

		for startMarker,stopMarker in pairwise(markers):
			digit = startMarker[0]
			(x1, y1, w1, h1) = cv2.boundingRect(startMarker[1])
			(x2, y2, w2, h2) = cv2.boundingRect(stopMarker[1])

			cropped = image[y1-(h1/2):y2+h2,x1+(w1+w2)/2:]
			cv2.imshow(str(digit),cropped)
			cv2.imwrite("cropped.png",cropped)
			text = ocr.convert("cropped.png")
			text = stripText(text)
			text = text.replace("\n"," ")
			text = unicode(text, "utf-8")
			results.append((digit,text))

		# convert the results list to notes
		text = listToText(results)
		print text

	cv2.waitKey(0)
if __name__ == '__main__':
  main()
