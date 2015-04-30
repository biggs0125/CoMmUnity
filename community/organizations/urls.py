from django.conf.urls import patterns, url
from django.contrib import admin
from organizations import views

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^create/$', views.CreateOrganization.as_view(), name='organization_create'),
)                 
                        
