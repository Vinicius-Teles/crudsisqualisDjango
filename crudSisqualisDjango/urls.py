from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crudSisqualisDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('users.urls')),
    url(r'^usuarios/', include('users.urls')),
    url(r'^usuarios/delete/(?P<project_id>\w+)/$', include('users.urls')),
    url(r'^usuarios/update/(?P<project_id>\w+)/$', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
