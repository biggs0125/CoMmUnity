from django.conf.urls import patterns, url, include
from django.contrib import admin
from apis.users import views

admin.autodiscover()

urlpatterns = patterns('',

        url(r'^login$', views.GetUser.as_view(), name='api_user_login'),

)
