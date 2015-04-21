from django.conf.urls import patterns, url
from django.contrib import admin
from calendars import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.DisplayCalendar.as_view(), name='calendars'),
)

