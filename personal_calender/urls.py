__author__ = 'Alexis'
from django.conf.urls import  patterns, url
from views import create, details, delete, delete_eve, update_eve
from personal_calender.views import Evenement_Liste

urlpatterns = patterns('',
    url(r'^create/$', create),
    url(r'^(\d+)/details/$',details),
    url(r'^(\d+)/participant/(\d+)/delete/$', delete),
    url(r'^listes/$', Evenement_Liste.as_view(paginate_by=10)),
    url(r'^(\d+)/delete/$', delete_eve),
    url(r'^(\d+)/update/$', update_eve),
    url(r'^listes/(?P<champs>[\w-]+)/(?P<terme>[\w-]+)/$', Evenement_Liste.as_view(paginate_by=10)),
)

