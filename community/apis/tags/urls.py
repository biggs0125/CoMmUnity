from django.conf.urls import patterns, url, include
from django.contrib import admin
from apis.tags import views

admin.autodiscover()

urlpatterns = patterns('',

        url(r'^retrieve$', views.GetTag.as_view(), name='api_tag_retrieve'),

)
