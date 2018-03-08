# -*- coding: utf-8 -*-
import time
import re
def transfer_pubtime(datetime):
    if re.match('\d+月\d+日', datetime):
        year = time.strftime('%Y',time.localtime())
        date = year + '年' + datetime
        datetime = date.replace(r'年', '-').replace(r'月', '-').replace(r'日', ' ') + ':00'
        #datetime = time.strftime('%Y', time.localtime()) + datetime + ':00'
    if re.match('\d+分钟前', datetime):
        minute = re.match('(\d+)', datetime).group(1)
        datetime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - float(minute) * 60)) + ':00'
    if re.match('今天.*', datetime):
        datetime = re.match('今天(.*)', datetime).group(1).strip()
        datetime = time.strftime("%Y-%m-%d", time.localtime()) + ' ' + datetime + ':00'
    print(datetime)

transfer_pubtime("今天00:34")
transfer_pubtime("40分钟前")
transfer_pubtime("01月20日18:30")
transfer_pubtime("2017-12-25 16:23:15")