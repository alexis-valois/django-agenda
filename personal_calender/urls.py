__author__ = 'Alexis'
from django.conf.urls import  patterns, include, url
from views import create

urlpatterns = patterns('',
    url(r'^create/$', create),
)