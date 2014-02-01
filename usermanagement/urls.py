__author__ = 'Alexis'
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import create_account
urlpatterns = patterns('',
    url(r'^succes/$', TemplateView.as_view(template_name="user/succes.html")),
    url(r'^create_account/$', create_account),
)