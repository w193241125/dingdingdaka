#!/usr/local/bin python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 12:21
# @Author  : Larwas
# @Link    : 164722305@qq.com
# @Site    : www.larwas.com
# @File    : test.py
# @Software: PyCharm
import os
import time
import urllib
import json

# 获取当前时间 格式20180213
# nowTime = time.strftime('%Y%m%d', time.localtime())
# date = nowTime
# print(date)
# # 节假日接口
# server_url = "http://api.goseek.cn/Tools/holiday?date="
#
# vop_url_request = urllib.request.Request(server_url + date)
# vop_response = urllib.request.urlopen(vop_url_request)
#
# vop_data = json.loads(vop_response.read())
# 打印返回的Json串
# print(vop_data['data'])
# 获取抖音app的com信息
get_com_info = r"aapt dump badging G:\python\dingding\AirDroid.apk > AirDroid.txt"
os.system(get_com_info)
with open("AirDroid.txt", "r", encoding="utf-8") as fs:
    donyin = fs.read()


#print(os.system(adbpng3))