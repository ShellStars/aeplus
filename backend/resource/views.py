# coding:utf-8
from django.http import HttpResponse
from models import *
from aeplus.tools import *

# Create your views here.
def taglist(requests):
    Resourceclasslist = Resourceclass.objects.all().values('id','name').order_by('ranking')
    total = Resourceclasslist.count()
    results = data_formatter(total=total,data_list=list(Resourceclasslist))
    return HttpResponse(results, content_type="application/json")


def resourcelist(requests):
    jsondata = json.loads(json.dumps(requests.GET))
    page_no = int(jsondata['page_no'])
    page_item = int(jsondata['page_item'])
    id = int(jsondata['id'])
    Resourceclasslist = Resourceinfo.objects.filter(column=id,published=True).values('logopic','name','link','summary').order_by('ranking')
    total = Resourceclasslist.count()
    Resourceclasslist = Resourceclasslist[(page_no - 1) * page_item:page_no * page_item]
    hosthead = requests.scheme + '://' + requests.get_host() + '/'
    for i in Resourceclasslist:
        i['logopic'] = hosthead + i['logopic']
    results = data_formatter(total=total,data_list=list(Resourceclasslist))
    return HttpResponse(results, content_type="application/json")
