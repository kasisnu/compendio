See the final-call.py to see how it works. Install dependencies:

NOTE: Dependencies have been checked only on Ubuntu 14.04 LTS

Setup Instructions for OpenCV on Ubuntu:

1. Open Terminal(Ctrl+Alt+T) and run these commands:

NOTE: Enter Y whenever prompted about package installation

	$ sudo apt-get update

	$ sudo apt-get install python-numpy

	$ sudo apt-get install python-scipy

	$ sudo apt-get install libopencv-*

	$ sudo apt-get install python-opencv

2. Download "https://bitbucket.org/3togo/python-tesseract/downloads/python-tesseract_0.9-0.5ubuntu3_trusty_amd64.deb"

3.	$ sudo apt-get install tesseract-ocr

4. Change working directory to the one where you have downloaded the file(see Step 2).

5.	$ sudo dpkg -i python-tesseract*.deb

	$ sudo apt-get -f install


Now, we have installed all dependencies for Tesseract OCR,
and are going to install the dependencies for handwriting recognition.

1.	$ sudo pip install -U networkx

2.	$ sudo pip install -U scikit-image

3.	$ pip install --user --install-option="--prefix=" -U scikit-learn

Done!

