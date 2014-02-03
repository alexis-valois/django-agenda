from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^user/', include('usermanagement.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^agenda/', include('personal_calender.urls')),
    )
