from django.conf.urls import patterns, url
from django.contrib import admin
from organizations import views

admin.autodiscover()

urlpatterns = patterns('',
        #url(r'^$', views.CreateEvent.as_view(), name='create'),
        url(r'^create/$', views.CreateEvent.as_view(), name='organization_create'),
)                 
                        