from django.conf.urls import patterns, url, include
from django.contrib import admin
from apis.events import views

admin.autodiscover()

urlpatterns = patterns('',

        url(r'^create$', views.CreateEvent.as_view(), name='api_event_create'),
        url(r'^retrieve$', views.GetEvent.as_view(), name='api_event_retrieve'),
        url(r'^add_attendee$', views.AddAttendee.as_view(), name='api_event_attend'),
)
