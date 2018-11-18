# coding:utf-8
from django.http import HttpResponse
import datetime
from models import *
from aeplus.tools import *

# Create your views here.
def bloglist(requests):
    bloginfo = Bloginfo.objects.filter(published=True).values('headpic','title','createtime').order_by('-createtime')[0:6]
    hosthead = requests.scheme + '://' + requests.get_host() + '/'
    for i in bloginfo:
        i['createtime'] = datetime.datetime.strftime(i['createtime'], '%Y.%m.%d')
        i['headpic'] = hosthead + i['headpic']
    results = data_formatter(data_list=list(bloginfo))
    return HttpResponse(results, content_type="application/json")