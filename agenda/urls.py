from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agenda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^user/', include('usermanagement.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout, {'next_page' : '/accounts/login'}),
    url(r'^accounts/profile/$', login_required(TemplateView.as_view(template_name="registration/profile.html"))),
 
)
