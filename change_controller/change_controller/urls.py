from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url, include
from change_requests.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RequestList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', RequestDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/(?P<version>\d+)$', RequestDetail.as_view(), name='detail-version'),
    #url(r'^create/(?P<template>\d+)$', RequestCreate.as_view(), name='create'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
