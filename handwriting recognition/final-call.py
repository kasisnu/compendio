# USAGE:
# python final-call.py --image images/deskew_marked_text.jpg


from hrandocr import getText
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True,
	help = "Path to image to be OCRed")
args = vars(ap.parse_args())

image = args["image"]

text = getText(image)

print text
