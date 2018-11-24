# coding:utf-8
from django.http import HttpResponse
from models import *
from aeplus.tools import *

# Create your views here.
def taglist(requests):
    Prolibclasslist = Prolibclass.objects.all().values('id','name').order_by('ranking')
    total = Prolibclasslist.count()
    results = data_formatter(total=total,data_list=list(Prolibclasslist))
    return HttpResponse(results, content_type="application/json")


def projectlist(requests):
    jsondata = json.loads(json.dumps(requests.GET))
    page_no = int(jsondata['page_no'])
    page_item = int(jsondata['page_item'])
    id = int(jsondata['id'])
    Instituteclasslist = Prolibinfo.objects.filter(column=id,published=True).values('logopic','name','summary','website').order_by('-createtime')
    total = Instituteclasslist.count()
    Instituteclasslist = Instituteclasslist[(page_no - 1) * page_item:page_no * page_item]
    hosthead = requests.scheme + '://' + requests.get_host() + '/'
    for i in Instituteclasslist:
        i['logopic'] = hosthead + i['logopic']
    results = data_formatter(total=total,data_list=list(Instituteclasslist))
    return HttpResponse(results, content_type="application/json")

