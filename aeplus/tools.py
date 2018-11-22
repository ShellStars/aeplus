# coding:utf-8
import json
from aeplus import settings
from subscribe.models import SubscribeUserList
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
# 附件部分
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
"""
    author:Lindow
    date:2018/11/18
"""
def data_formatter(total=None,data_list=None, message="success", status=2000):
    results = {
        "message": message,
        "status": status,
        "result": {}
    }

    if isinstance(data_list, list):
        results["total"] = total
        results["result"]["datas"] = data_list
    print json.dumps(results)
    return json.dumps(results,ensure_ascii=False)


def send_email(emailtitle,content):
    # msg = MIMEText('<html><body><h1>hello</h1>' +
    #               '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    #               '</body></html>', 'html', 'utf-8')
    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = Header(u'AeternityPlus社区', 'utf-8').encode()
    # msg['To'] = Header(u'AeternityPlus Fans', 'utf-8').encode()
    msg['Subject'] = Header(emailtitle, 'utf-8').encode()
    try:
        TO_ADDR = SubscribeUserList.objects.filter(status=True).values_list('email',flat=True)
        smtpObj = smtplib.SMTP()
        smtpObj.connect(settings.SMTP_SERVER, 25)
        smtpObj.login(settings.FROM_ADDR, settings.PASSWORD)
        smtpObj.sendmail(settings.FROM_ADDR, TO_ADDR, msg.as_string())
        return True
    except smtplib.SMTPException:
        return False
