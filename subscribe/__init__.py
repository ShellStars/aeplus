# coding:utf-8
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from subscribe.models import *
from aeplus.tools import send_email


@receiver(post_init, sender=Subscribeinfo)
def post_init_func(instance, sender, **kwargs):
    instance.__original = instance.published


@receiver(post_save, sender=Subscribeinfo)
def post_save_func(instance, sender,**kwargs):
    if instance.__original == False and instance.published == True:
        title = instance.emailtitle
        content = instance.content
        send_email(title,content)

