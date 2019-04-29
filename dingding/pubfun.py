#!/usr/local/bin python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 14:21
# @Author  : Larwas
# @Link    : 164722305@qq.com
# @Site    : www.larwas.com
# @File    : pubfun.py
# @Software: PyCharm
import os
import time


def mormning(_self_, current_time):
    donyin_package_name = "com.alibaba.android.rimet"
    douyin_activity_name = "com.alibaba.android.rimet.biz.SplashActivity"
    tap_place = "adb  shell input tap 363 1219"
    tap_place_kaoqin = "adb  shell input tap 272 724"
    tap_place_daka = "adb  shell input tap 185 1234"
    tap_place_shangban = "adb  shell input tap 353 499"
    tap_place_xiaban = "adb  shell input tap 353 756"


    start_app = f"adb shell am start -n {donyin_package_name}/{douyin_activity_name}"

    print("启动dd")
    os.system(start_app)

    # 操作钉钉
    os.system(tap_place)
    os.system(tap_place_kaoqin)
    time.sleep(5)
    os.system(tap_place_daka)
    time.sleep(5)

    if current_time < "09:30":
        os.system(tap_place_shangban)
        print(1)
    else:
        os.system(tap_place_xiaban)
        print(2)



