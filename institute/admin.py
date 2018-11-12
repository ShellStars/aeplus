# coding:utf-8
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Instituteclass, Instituteinfo


class InstituteclassAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'ranking', 'createtime', 'updatetime','do_data')
    def do_data(self, obj):
        return mark_safe(u'<a href={}/delete/ />删除&nbsp;&nbsp;&nbsp;&nbsp;<a href={}/ />编辑'.format(obj.id,obj.id))
    do_data.short_description = '操作'


class InstituteinfoAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'ranking','column', 'createtime', 'updatetime', 'published','headpic_data','do_data')
    readonly_fields = ('headpic_data',)
    def headpic_data(self, obj):
        return mark_safe(u'<img src="%s" width="100px" />' % obj.headpic.url)
    headpic_data.short_description = '头像'
    def do_data(self, obj):
        return mark_safe(u'<a href={}/delete/ />删除&nbsp;&nbsp;&nbsp;&nbsp;<a href={}/ />编辑'.format(obj.id,obj.id))
    do_data.short_description = '操作'
    search_fields = ('name',)


admin.site.register(Instituteclass, InstituteclassAdmin)
admin.site.register(Instituteinfo, InstituteinfoAdmin)