# coding:utf-8
from django.http import HttpResponse
import datetime
import json
from models import *
from aeplus.tools import *

# Create your views here.
def bloglist(requests):
    jsondata = json.loads(requests.body)
    page_no = jsondata['page_no']
    page_item = jsondata['page_item']
    bloginfo = Bloginfo.objects.filter(published=True).values('headpic','title','createtime').order_by('-createtime')
    total = bloginfo.count()
    bloginfo = bloginfo[(page_no-1)*page_item:page_no*page_item]
    hosthead = requests.scheme + '://' + requests.get_host() + '/'
    for i in bloginfo:
        i['node_time'] = datetime.datetime.strftime(i['createtime'], '%Y.%m.%d')
        i['headpic'] = hosthead + i['headpic']
        i['node_title'] = i['title']
        del i['createtime']
        del i['title']
    results = data_formatter(total=total, data_list=list(bloginfo))
    return HttpResponse(results, content_type="application/json")