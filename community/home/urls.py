from django.conf.urls import patterns, url
from django.contrib import admin
from home import views

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^create/$', views.CreateEvent.as_view(), name='home'),
)
