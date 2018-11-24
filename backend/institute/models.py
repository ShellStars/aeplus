# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Instituteclass(models.Model):
    name = models.CharField('分类', max_length=20)
    ranking = models.IntegerField('顺序', unique=True, blank=False)
    createtime = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    updatetime = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '研究院分类管理'
        verbose_name_plural = '研究院分类管理'
        ordering = ['createtime']


@python_2_unicode_compatible
class Instituteinfo(models.Model):
    headpic = models.ImageField('头像', upload_to='uploads/images/institute/')
    name = models.CharField('姓名', max_length=40)
    summary = models.TextField('简介', default='', blank=False, )
    column = models.ForeignKey(Instituteclass, verbose_name='分类')
    ranking = models.IntegerField('顺序', unique=True, blank=False)
    createtime = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    updatetime = models.DateTimeField('更新时间', auto_now=True)
    published = models.BooleanField('正式发布', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '会员'
        verbose_name_plural = '会员'


@python_2_unicode_compatible
class Schoolinfo(models.Model):
    logopic = models.ImageField('校标', upload_to='uploads/images/school/')
    name = models.CharField('学校名称', max_length=40)
    # column = models.ForeignKey(Instituteclass, verbose_name='分类')
    # ranking = models.IntegerField('顺序', unique=True, blank=False)
    createtime = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    updatetime = models.DateTimeField('更新时间', auto_now=True)
    published = models.BooleanField('正式发布', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '院校'
        verbose_name_plural = '院校'