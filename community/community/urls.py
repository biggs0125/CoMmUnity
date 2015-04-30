from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'community.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('apis.urls')),
    url(r'^event/', include('events.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^calendar/', include('calendars.urls')),
    url(r'^organization/', include('organizations.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
)
