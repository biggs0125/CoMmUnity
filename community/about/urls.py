from django.conf.urls import patterns, url
from django.contrib import admin
from about import views

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', views.AboutUs.as_view(), name='about_us'),
)
