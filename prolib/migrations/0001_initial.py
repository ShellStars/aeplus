# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prolibclass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('ranking', models.IntegerField(unique=True, verbose_name='\u987a\u5e8f')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'ordering': ['createtime'],
                'verbose_name': '\u9879\u76ee\u5e93\u5206\u7c7b\u7ba1\u7406',
                'verbose_name_plural': '\u9879\u76ee\u5e93\u5206\u7c7b\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Prolibinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logopic', models.ImageField(upload_to='uploads/images/prolib/', verbose_name='LOGO')),
                ('name', models.CharField(max_length=40, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('summary', models.TextField(default='', verbose_name='\u7b80\u4ecb')),
                ('website', models.URLField(verbose_name='\u5b98\u7f51')),
                ('ranking', models.IntegerField(unique=True, verbose_name='\u987a\u5e8f')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('published', models.BooleanField(default=True, verbose_name='\u6b63\u5f0f\u53d1\u5e03')),
                ('column', models.ForeignKey(verbose_name='\u5206\u7c7b', to='prolib.Prolibclass')),
            ],
            options={
                'verbose_name': '\u9879\u76ee',
                'verbose_name_plural': '\u9879\u76ee',
            },
        ),
    ]
