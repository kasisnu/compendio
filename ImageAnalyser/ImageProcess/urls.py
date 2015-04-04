from django.conf.urls import patterns, url

from ImageProcess import views

urlpatterns = patterns('',
    url(r'^upload/', views.inputimage, name='inputimage')
)
