from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def inputimage(request):
    if request.method == 'POST':
        imagePath = 'Test.jpg'
        destination = open(imagePath, 'wb+')
        for chunk in request.FILES['photo'].chunks():
            destination.write(chunk)
        destination.close()
        return HttpResponse("Hello, I hope the image is saved.")

# Create your views here.
