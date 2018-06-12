#!/usr/bin/python
# -*- coding: UTF-8 -*-
from aliyunsdkcore import client
from aliyunsdkcms.request.v20180308 import QueryMetricListRequest
import re
import datetime
import time
clt = client.AcsClient('LTAI06yiYnIsoiiV','XvEpCLeFyRsDhKamlScTXmbYzq5ErI', 'cn-hangzhou')
request = QueryMetricListRequest.QueryMetricListRequest()
request.set_accept_format('json')
request.set_Project('acs_cen')
request.set_Metric('InternetOutRateByConnectionRegion')
#start_time = "2018-06-06 16:22:00"
start_time = (datetime.datetime.now()-datetime.timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")
timestamp_start = int(time.mktime(time.strptime(start_time, "%Y-%m-%d %H:%M:%S"))) * 1000
request.set_StartTime(timestamp_start)
request.set_Dimensions('{"cenId":"cen-pfqkdplbeeogk9finu","geographicSpanId":"china_china","localRegionId":"cn-hangzhou","oppositeRegionId":"cn-shanghai"}')
request.set_Period('60')
result = clt.do_action_with_exception(request)
#print result
aa = result.split('}')[-3].split(':')[-1]
print float(aa)
#bb = float(aa)/1024/1024
#print float('%.2f' % bb)
