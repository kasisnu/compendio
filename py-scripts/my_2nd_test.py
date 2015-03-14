# Basic Full Page OCR generating HTML
# usage: python mytest.py --image <Path to image>

from imtotext import OCR
import argparse

# parsing console arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

image = args["image"]

# initialize the OCR engine
ocr = OCR()

result = ocr.convert(image)

htmlResult = "<html>" + result.replace("\n"," ") + "</html>"
fileObject = open("htmlOut.html","wb")
fileObject.write(htmlResult)
fileObject.close()
