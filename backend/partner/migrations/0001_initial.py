# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partnerinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logopic', models.ImageField(upload_to='uploads/images/partner/', verbose_name='LOGO')),
                ('name', models.CharField(max_length=40, verbose_name='\u540d\u79f0')),
                ('link', models.URLField(verbose_name='\u94fe\u63a5')),
                ('ranking', models.IntegerField(unique=True, verbose_name='\u987a\u5e8f')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('published', models.BooleanField(default=True, verbose_name='\u6b63\u5f0f\u53d1\u5e03')),
            ],
            options={
                'verbose_name': '\u5408\u4f5c\u4f19\u4f34',
                'verbose_name_plural': '\u5408\u4f5c\u4f19\u4f34',
            },
        ),
    ]
