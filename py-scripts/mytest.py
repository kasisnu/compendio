# Basic Full Page OCR generating HTML


import tesseract
import ctypes
import os
api = tesseract.TessBaseAPI()
api.SetOutputName("outputName");
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetPageSegMode(tesseract.PSM_AUTO)
mImgFile = "testcases/multi-para.png"

result = tesseract.ProcessPagesWrapper(mImgFile,api)
htmlResult = "<html>" + result.replace("\n"," ") + "</html>"
fileObject = open("htmlOut.html","wb")
fileObject.write(htmlResult)
fileObject.close()
