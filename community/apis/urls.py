from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

        url(r'^event/', include('apis.events.urls')),
        url(r'^tag/', include('apis.tags.urls')),
        url(r'^user/', include('apis.users.urls')),
        url(r'^organization/', include('apis.organizations.urls')),


)
