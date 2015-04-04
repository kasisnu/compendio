from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import sys
import os.path
sys.path.insert(0, 'script')
from hrandocr import getText
from random import randint

@csrf_exempt
def inputimage(request):
    if request.method == 'POST':
        
        #Giving a random name to file that doesnot exists in the image buffer
        originalname = request.FILES['photo'].name
        if '.png' in originalname:
            ext = '.png'
        else:
            ext = '.jpg' 
        imagePath = 'imgbuffer/' + str(randint(1,10000)) + ext
        while os.path.isfile(imagePath):
            imagePath = 'imgbuffer/' + str(randint(1,10000)) + ext

        #Writing the file in the image buffer
        destination = open(imagePath, 'wb+')
        for chunk in request.FILES['photo'].chunks():
            destination.write(chunk)
        destination.close()
        #Initialize the OCR engine and getting result
        text = getText(imagePath)

	#Deleting file from image buffer and sending the response back
	os.remove(imagePath)
        return HttpResponse(text)

# Create your views here.
