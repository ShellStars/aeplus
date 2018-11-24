# coding:utf-8
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Blogclass, Bloginfo


class BlogclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'ranking', 'createtime', 'updatetime','do_data')
    def do_data(self, obj):
        return mark_safe(u'<a href={}/delete/ />删除&nbsp;&nbsp;&nbsp;&nbsp;<a href={}/ />编辑'.format(obj.id,obj.id))
    do_data.short_description = '操作'


class BloginfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'createtime', 'updatetime', 'published','do_data')
    readonly_fields = ('headpic_data',)

    def headpic_data(self, obj):
        return mark_safe(u'<img src="%s" width="100px" />' % obj.headpic.url)

    headpic_data.short_description = 'LOGO'

    def do_data(self, obj):
        return mark_safe(u'<a href={}/delete/ />删除&nbsp;&nbsp;&nbsp;&nbsp;<a href={}/ />编辑'.format(obj.id, obj.id))

    do_data.short_description = '操作'
    search_fields = ('name',)


admin.site.register(Blogclass, BlogclassAdmin)
admin.site.register(Bloginfo, BloginfoAdmin)