__author__ = 'Alexis'
from django.conf.urls import  patterns, include, url
from views import create, details

urlpatterns = patterns('',
    url(r'^create/$', create),
    url(r'^(\d+)/details/$',details),
)