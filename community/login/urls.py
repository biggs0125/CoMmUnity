from django.conf.urls import patterns, url
from django.contrib import admin
from login import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
)
