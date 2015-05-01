from django.conf.urls import patterns, url
from django.contrib import admin
from tags import views

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^subscribe$', views.SubscribeView.as_view(), name='tag_subscribe'),
)
