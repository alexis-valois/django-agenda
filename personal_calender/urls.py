__author__ = 'Alexis'
from django.conf.urls import  patterns, url
from views import create, details, delete, liste, delete_eve, update_eve

urlpatterns = patterns('',
    url(r'^create/$', create),
    url(r'^(\d+)/details/$',details),
    url(r'^(\d+)/participant/(\d+)/delete/$', delete),
    url(r'^liste/$', liste),
    url(r'^(\d+)/delete/$', delete_eve),
    url(r'^(\d+)/update/$', update_eve),
)

