# coding:utf-8
from django.http import HttpResponse
from models import *
from aeplus.tools import *

# Create your views here.
def institutelist(requests):
    Instituteclasslist = Instituteclass.objects.all().values('id','name').order_by('ranking')
    mixdata = {int(k['id']):str(k['name']) for k in Instituteclasslist}
    result = []
    for i in mixdata.keys():
        dic = {}
        itemsinfo = Instituteinfo.objects.filter(published=True,column=i).values('headpic','name','summary').order_by('ranking')
        hosthead = requests.scheme + '://' + requests.get_host() + '/'
        for j in itemsinfo:
            j['headpic'] = hosthead + j['headpic']
        dic[mixdata[i]] = list(itemsinfo)
        result.append(dic)
    results = data_formatter(data_list=list(result))
    return HttpResponse(results, content_type="application/json")
