# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Blogclass(models.Model):
    name = models.CharField('分类名称', max_length=20)
    ranking = models.IntegerField('顺序', unique=True, blank=False)
    createtime = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    updatetime = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客分类管理'
        verbose_name_plural = '博客分类管理'
        ordering = ['createtime']


@python_2_unicode_compatible
class Bloginfo(models.Model):
    headpic = models.ImageField('封面', upload_to='uploads/images/blog/')
    column = models.ForeignKey(Blogclass, verbose_name='分类')
    title = models.CharField('标题', max_length=40)
    content = UEditorField('详情', height=300, width=700,
                           default=u'', blank=True, imagePath="uploads/images/blog/",
                           toolbars='besttome', filePath='uploads/files/blog/')
    createtime = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    updatetime = models.DateTimeField('更新时间', auto_now=True)
    published = models.BooleanField('正式发布', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '资讯'
        verbose_name_plural = '资讯'

