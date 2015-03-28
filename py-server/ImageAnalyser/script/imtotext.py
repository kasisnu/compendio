# Basic Full Page OCR generating HTML

import tesseract

class OCR:
	def __init__(self):
		# setting up the Tesseract API
		self.api = tesseract.TessBaseAPI()
		self.api.SetOutputName("outputName");
		self.api.Init(".","eng",tesseract.OEM_DEFAULT)
		self.api.SetPageSegMode(tesseract.PSM_AUTO)

	def convert(self, image):
		result = tesseract.ProcessPagesWrapper(image,self.api)
		return result
