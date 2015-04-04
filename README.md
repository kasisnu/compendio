## Summary

The official repository for the project "**Extraction of selected text from scanned documents**", codenamed "**Compendio**".


To install **compendio**  dependencies system-wide:

```
#!bash
$ sudo apt-get update
$ sudo apt-get install python-numpy
$ sudo apt-get install python-scipy
$ sudo apt-get install libopencv-*
$ sudo apt-get install python-opencv
$ sudo apt-get install python-django
```

Download "https://bitbucket.org/3togo/python-tesseract/downloads/python-tesseract_0.9-0.5ubuntu3_trusty_amd64.deb"


```
#!bash

$ sudo dpkg -i python-tesseract*.deb
$ sudo apt-get -f install
$ sudo pip install -U networkx
$ sudo pip install -U scikit-image
$ pip install --user --install-option="--prefix=" -U scikit-learn
```

Run the Django server by changing working directory to ImageAnalyser, and then

```
#!bash

$ python manage.py runserver 0.0.0.0:8000
```

Now use the TestFormPage.html to check if everything is installed correctly.