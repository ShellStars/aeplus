# coding:utf-8
from django.http import HttpResponse
from models import *
from aeplus.tools import *

# Create your views here.


def taglist(requests):
    Instituteclasslist = Instituteclass.objects.all().values('id','name').order_by('ranking')
    total = Instituteclasslist.count()
    results = data_formatter(total=total,data_list=list(Instituteclasslist))
    return HttpResponse(results, content_type="application/json")


def institutelist(requests):
    jsondata = json.loads(json.dumps(requests.GET))
    page_no = int(jsondata['page_no'])
    page_item = int(jsondata['page_item'])
    id = int(jsondata['id'])
    Instituteclasslist = Instituteinfo.objects.filter(column=id,published=True).values('headpic','name','summary').order_by('ranking')
    total = Instituteclasslist.count()
    Instituteclasslist = Instituteclasslist[(page_no - 1) * page_item:page_no * page_item]
    hosthead = requests.scheme + '://' + requests.get_host() + '/'
    for i in Instituteclasslist:
        i['headpic'] = hosthead + i['headpic']
    results = data_formatter(total=total,data_list=list(Instituteclasslist))
    return HttpResponse(results, content_type="application/json")


def schoolinfo(requests):
    shinfo = Schoolinfo.objects.filter(published=True).values('logopic','name').order_by('-createtime')
    total = shinfo.count()
    hosthead = requests.scheme + '://' + requests.get_host() + '/'
    for i in shinfo:
        i['img_url'] = hosthead + i['logopic']
        del i['logopic']
    results = data_formatter(total=total, data_list=list(shinfo))
    return HttpResponse(results, content_type="application/json")