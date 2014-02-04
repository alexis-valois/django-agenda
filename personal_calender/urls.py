__author__ = 'Alexis'
from django.conf.urls import  patterns, url
from views import create, details, delete

urlpatterns = patterns('',
    url(r'^create/$', create),
    url(r'^(\d+)/details/$',details),
    url(r'^(\d+)/participant/(\d+)/delete/$', delete),
)

