from django.conf.urls import patterns, url, include
from django.contrib import admin
from apis.users import views

admin.autodiscover()

urlpatterns = patterns('',

        url(r'^login$', views.GetUser.as_view(), name='api_user_login'),
        url(r'^add_subscriptions', views.AddSubscriptions.as_view(), name='api_user_add_subscription'),
        url(r'^get_subscriptions', views.GetSubscriptions.as_view(), name='api_user_get_subscription'),


)
