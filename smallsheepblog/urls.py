#!/usr/bin/python
#coding:utf-8

import settings

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smallsheepblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','engine.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sub_page/$','engine.views.subPage'),	


)

if settings.DEBUG is True:
    urlpatterns += staticfiles_urlpatterns()
