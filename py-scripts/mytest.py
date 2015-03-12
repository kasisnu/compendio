# Basic Full Page OCR generating HTML
# usage: python mytest.py --image <Path to image>

import tesseract
import ctypes
import os
import argparse

# parsing console arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

image = args["image"]

# setting up the Tesseract API
api = tesseract.TessBaseAPI()
api.SetOutputName("outputName");
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetPageSegMode(tesseract.PSM_AUTO)

result = tesseract.ProcessPagesWrapper(image,api)
htmlResult = "<html>" + result.replace("\n"," ") + "</html>"
fileObject = open("htmlOut.html","wb")
fileObject.write(htmlResult)
fileObject.close()
