# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class SubscribeUserList(models.Model):
    email = models.EmailField('邮箱', unique=True, blank=False)
    status = models.BooleanField('是否订阅', default=True)
    createtime = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    updatetime = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = '订阅邮箱'
        verbose_name_plural = '订阅邮箱'
        ordering = ['createtime']


@python_2_unicode_compatible
class Subscribeinfo(models.Model):
    emailtitle = models.CharField('标题', blank=False, max_length=40)
    content = UEditorField('正文', height=300, width=700,
                           default=u'', blank=False, imagePath="uploads/images/subscribe/",
                           toolbars='besttome', filePath='uploads/files/subscribe/')
    createtime = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    updatetime = models.DateTimeField('更新时间', auto_now=True)
    published = models.BooleanField('正式发布', default=False)

    def __str__(self):
        return self.emailtitle

    class Meta:
        verbose_name = '订阅文章'
        verbose_name_plural = '订阅文章'

