# coding:utf-8
from django.http import HttpResponse
from models import *
from aeplus.tools import *

# Create your views here.
def parnterlist(requests):
    jsondata = json.loads(json.dumps(requests.GET))
    page_no = int(jsondata['page_no'])
    page_item = int(jsondata['page_item'])
    partnerinfo = Partnerinfo.objects.filter(published=True).values('logopic','name','link').order_by('ranking')
    total = partnerinfo.count()
    partnerinfo = partnerinfo[(page_no - 1) * page_item:page_no * page_item]
    hosthead = requests.scheme + '://' + requests.get_host() + '/'
    for i in partnerinfo:
        i['logopic'] = hosthead + i['logopic']
    results = data_formatter(total=total,data_list=list(partnerinfo))
    return HttpResponse(results, content_type="application/json")