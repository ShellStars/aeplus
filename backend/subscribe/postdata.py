# coding:utf-8
"""
    author:Lindow
    date:2018/11/18
"""
import requests
import json
url = "http://127.0.0.1:8000/subscribe/addsubscribe/"
data = {"email":"125@123.com"}
a = requests.post(url,json.dumps(data))
print a
