__author__ = 'Alexis'
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
urlpatterns = patterns('',
    url(r'^succes/$', TemplateView.as_view(template_name="user/succes.html"))
)