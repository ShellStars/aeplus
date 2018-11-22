# coding:utf-8
"""
    author:Lindow
    date:2018/11/18
"""
from django.conf.urls import patterns, url, include
from .views import *
from aeplus import settings
urlpatterns = patterns('',
    url(r'^get_partner_list/', parnterlist, name='parnterlist'),
)