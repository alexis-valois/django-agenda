__author__ = 'Alexis'
from django.conf.urls import  patterns, url
from views import create, details, delete, liste, delete_eve, update_eve
from django.views.generic import ListView
from models import Evenement

urlpatterns = patterns('',
    url(r'^create/$', create),
    url(r'^(\d+)/details/$',details),
    url(r'^(\d+)/participant/(\d+)/delete/$', delete),
    url(r'^liste/$', liste),
    url(r'^listes/$', ListView.as_view(model=Evenement, paginate_by=10)),
    url(r'^(\d+)/delete/$', delete_eve),
    url(r'^(\d+)/update/$', update_eve),
)

