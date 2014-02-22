__author__ = 'Alexis'
from django.conf.urls import patterns, url
from views import InvitationListView, InvitationView


urlpatterns = patterns('',
    url(r'^invitations/$', InvitationListView.as_view(), name='invitation_liste'),
    url(r'^invitation/$', InvitationView.as_view(), name='invitation_liste'),
)