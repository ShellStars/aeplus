# coding:utf-8
from django.http import HttpResponse
from models import *
from aeplus.tools import *

# Create your views here.
def parnterlist(requests):
    partnerinfo = Partnerinfo.objects.filter(published=True).values('logopic','name','link').order_by('ranking')[0:16]
    hosthead = requests.scheme + '://' + requests.get_host() + '/'
    for i in partnerinfo:
        i['logopic'] = hosthead + i['logopic']
    results = data_formatter(data_list=list(partnerinfo))
    return HttpResponse(results, content_type="application/json")