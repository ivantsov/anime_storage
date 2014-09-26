from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('apps.main.urls')),
    url(r'^api/', include('apps.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)