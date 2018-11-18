# coding:utf-8
"""
    author:Lindow
    date:2018/11/18
"""
from django.conf.urls import patterns, url, include
from .views import *
from aeplus import settings
urlpatterns = patterns('',
    url(r'^list/', bloglist, name='bloglist'),
)