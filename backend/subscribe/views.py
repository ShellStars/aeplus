# coding:utf-8
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import *
from aeplus.tools import *
import json
# Create your views here.


@csrf_exempt
def addsubscribe(requests):
    if requests.method == "POST":
        jsondata = json.loads(requests.body)
        if "email" in jsondata.keys():
            if jsondata['email'].strip() != "":
                emaildata = jsondata['email']
                databaseemail = SubscribeUserList.objects.filter(email=str(emaildata))
                if databaseemail.count() > 0:
                    if databaseemail[0].status is False:
                        databaseemail.update(status=True)
                        results = data_formatter(message="Subscribe successful")
                        return HttpResponse(results, content_type="application/json")
                    else:
                        results = data_formatter(message="Subscribe successful")
                        return HttpResponse(results, content_type="application/json")
                else:
                    SubscribeUserList.objects.create(email=str(emaildata))
                    results = data_formatter(message="Subscribe successful")
                    return HttpResponse(results, content_type="application/json")
            else:
                results = data_formatter(message="Email can not be empty", status=4031)
                return HttpResponse(results, content_type="application/json")
        else:
            results = data_formatter(message="Params is not correct", status=403)
            return HttpResponse(results, content_type="application/json")
    else:
        results = data_formatter(message="Method is not allowed",status=405)
        return HttpResponse(results, content_type="application/json")
