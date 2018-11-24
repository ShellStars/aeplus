# coding:utf-8
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import SubscribeUserList, Subscribeinfo


class SubscribeUserListAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'status', 'createtime', 'updatetime','do_data')
    def do_data(self, obj):
        return mark_safe(u'<a href={}/delete/ />删除&nbsp;&nbsp;&nbsp;&nbsp;<a href={}/ />编辑'.format(obj.id,obj.id))
    do_data.short_description = '操作'
    search_fields = ('email',)

class SubscribeinfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'emailtitle', 'createtime', 'updatetime', 'published','do_data')

    def do_data(self, obj):
        return mark_safe(u'<a href={}/delete/ />删除&nbsp;&nbsp;&nbsp;&nbsp;<a href={}/ />编辑'.format(obj.id, obj.id))

    do_data.short_description = '操作'
    search_fields = ('emailtitle',)


admin.site.register(SubscribeUserList, SubscribeUserListAdmin)
admin.site.register(Subscribeinfo, SubscribeinfoAdmin)