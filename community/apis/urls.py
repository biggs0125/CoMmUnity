from django.conf.urls import patterns, url
from django.contrib import admin
from apis import views

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^event/create/$', views.CreateEvent.as_view(), name='api_event_create'),
)
