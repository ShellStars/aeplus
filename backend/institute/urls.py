# coding:utf-8
"""
    author:Lindow
    date:2018/11/18
"""
from django.conf.urls import patterns, url, include
from .views import *
from aeplus import settings
urlpatterns = patterns('',
    url(r'^get_tag_list/', taglist, name='taglist'),
    url(r'^get_relation_list/', institutelist, name='institutelist'),
    url(r'^school_info/', schoolinfo, name='schoolinfo'),
)