__author__ = 'Alexis'
from django.conf.urls import  patterns, url
from views import delete
from personal_calender.views import Evenement_Liste, Evenement_Detail
from models import Evenement
from django.views.generic import CreateView, UpdateView, DeleteView
from forms import EventForm
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
    url(r'^create/$', CreateView.as_view(model=Evenement, form_class=EventForm)),
    url(r'^(?P<pk>\d+)/update/$', UpdateView.as_view(model=Evenement, form_class=EventForm)),
    url(r'^(\d+)/participant/(\d+)/delete/$', delete),
    url(r'^(?P<pk>\d+)/delete/$', DeleteView.as_view(model=Evenement, success_url=reverse_lazy('liste')), name="delete"),
    url(r'^listes/$', Evenement_Liste.as_view(paginate_by=10), name='liste'),
    url(r'^listes/(?P<champs>[\w-]+)/(?P<terme>[\w-]+)/$', Evenement_Liste.as_view(paginate_by=10)),
    url(r'^(?P<pk>\d+)/detail/$', Evenement_Detail.as_view(template_name='personal_calender/event/details.html'), name="details"),
)

