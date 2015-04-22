from django.conf.urls import patterns, url, include
from django.contrib import admin
from apis.organizations import views

admin.autodiscover()

urlpatterns = patterns('',

        url(r'^create$', views.CreateOrganization.as_view(), name='api_create_organization'),
        url(r'^retrieve$', views.GetOrganizations.as_view(), name='api_retrieve_organization'),
        url(r'^get_admins$', views.GetAdmins.as_view(), name='api_get_admins'),
        url(r'^add_admin$', views.AddAdmin.as_view(), name='api_add_admin'),

)

