# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from myproject.myapp.views import *

urlpatterns = patterns('myproject.myapp.views',
                       url(r'^search/$', 'search'),
                       url(r'^list/$', 'list', name='list'),
                       )
