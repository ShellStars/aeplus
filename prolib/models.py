# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Prolibclass(models.Model):
    name = models.CharField('分类名称', max_length=20)
    ranking = models.IntegerField('顺序', unique=True, blank=False)
    createtime = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    updatetime = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目库分类管理'
        verbose_name_plural = '项目库分类管理'
        ordering = ['createtime']


@python_2_unicode_compatible
class Prolibinfo(models.Model):
    logopic = models.ImageField('LOGO', upload_to='uploads/images/prolib/')
    name = models.CharField('项目名称', max_length=40)
    summary = models.TextField('简介', default='', blank=False)
    website = models.URLField('官网')
    column = models.ForeignKey(Prolibclass, verbose_name='分类')
    ranking = models.IntegerField('顺序', unique=True, blank=False)
    createtime = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    updatetime = models.DateTimeField('更新时间', auto_now=True)
    published = models.BooleanField('正式发布', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'

