# coding:utf-8
from django.http import HttpResponse
from models import *
from aeplus.tools import *

# Create your views here.
def resourcelist(requests):
    Resourceclasslist = Resourceclass.objects.all().values('id','name').order_by('ranking')
    mixdata = {int(k['id']):str(k['name']) for k in Resourceclasslist}
    result = []
    for i in mixdata.keys():
        dic = {}
        itemsinfo = Resourceinfo.objects.filter(published=True,column=i).values('logopic','name','link','summary').order_by('ranking')
        hosthead = requests.scheme + '://' + requests.get_host() + '/'
        for j in itemsinfo:
            j['logopic'] = hosthead + j['logopic']
        dic[mixdata[i]] = list(itemsinfo)
        result.append(dic)
    results = data_formatter(data_list=list(result))
    return HttpResponse(results, content_type="application/json")
