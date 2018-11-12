# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Partnerinfo(models.Model):
    logopic = models.ImageField('LOGO', upload_to='uploads/images/partner/')
    name = models.CharField('名称', max_length=40)
    link = models.URLField('链接', blank=False)
    ranking = models.IntegerField('顺序', unique=True, blank=False)
    createtime = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    updatetime = models.DateTimeField('更新时间', auto_now=True)
    published = models.BooleanField('正式发布', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '合作伙伴'
        verbose_name_plural = '合作伙伴'

