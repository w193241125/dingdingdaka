#!/usr/local/bin python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 10:38
# @Author  : Larwas
# @Link    : 164722305@qq.com
# @Site    : www.larwas.com
# @File    : dingding.py
# @Software: PyCharm
import os
import re
import time
import urllib
import json
import requests

# nameplt = re.compile("package: name='(.*?)' versionCode")
# activityplt = re.compile("launchable-activity: name='(.*?)'")
adbshell = "adb shell"  # 启用shell命令可以直接操作Android系统
# adbstr = "adb push D:/1.txt /mnt/txt/1.txt"  # 把电脑的文件推送到安卓
# adbpng1 = "adb pull /sdcard/screencap.png d://"
# adbpng2 = "adb pull /sdcard/screencap.png d://1.png"
# adb_use_screencap = "adb shell /system/bin/screencap -p /sdcard/667.png"  # 截取安卓的屏幕
# adbpng3 = "adb pull /sdcard/667.png d://3.png"  # 把安卓的截图导入到电脑
# get_app_info = "adb shell pm list packages"  # 获取模拟器所有包名
tap_place_index = "adb  shell input tap 78 1219"
tap_place = "adb  shell input tap 363 1219"
tap_place_kaoqin = "adb  shell input tap 272 724"
tap_place_kaoqin2 = "adb  shell input tap 268 1051"
tap_place_daka = "adb  shell input tap 185 1234"
tap_place_shangban = "adb  shell input tap 353 499"
tap_place_xiaban = "adb  shell input tap 353 756"
wake_up = "adb shell input keyevent 26"
unlock = "adb shell input  swipe 370 952 370 318"
wrap_a = "adb shell input  swipe 370 318 370 952"
shut_up = "adb shell input tap 661 588"  # 收起
return_a = "adb  shell input tap 52 101"
return_b = "adb  shell input tap 156 101"
return_ding_index = "adb  shell input tap 75 1224"
return_index = "adb shell input keyevent 3"
turnback = "adb shell input keyevent 4"
donyin_package_name = "com.alibaba.android.rimet"
douyin_activity_name = "com.alibaba.android.rimet.biz.SplashActivity"
power_stat = "adb shell dumpsys window policy"
kill_dingding = "adb shell am force-stop com.alibaba.android.rimet"

# 获取抖音app的com信息
# get_com_info = r"aapt dump badging G:\python\dingding\rimet.apk > dingding.txt"
# os.system(get_com_info)
# with open("dingding.txt", "r", encoding="utf-8") as fs:
#     donyin = fs.read()
#
# donyin_package_name = nameplt.findall(donyin)[0]
# douyin_activity_name = activityplt.findall(donyin)[0]
#
# print("钉钉activity", douyin_activity_name)
# print("钉钉的包名", donyin_package_name)
# os.system(adb_use_screencap)
# #print(os.system(adbpng3))

start_app = f"adb shell am start -n {donyin_package_name}/{douyin_activity_name}"
start_airdroid = f"adb shell am start -n com.sand.airdroid/com.sand.airdroid.ui.splash.SplashActivity_"

# 获取当前周数
current_week = time.strftime("%W")
# 取余 当前1为双休0为单休
mod = int(current_week) % 2
# 获取今天周几
current_weekday = time.strftime("%w", time.localtime())
# 获取当前时间
current_time = time.strftime('%H:%M', time.localtime(time.time()))


def isAwaked(deviceid = ''):
    '''
    判断的依据是'    mAwake=false\n'
    '''
    if deviceid == '':
        cmd = 'adb shell dumpsys window policy'
    else:
        cmd = 'adb -s ' + deviceid + ' shell dumpsys window policy'
    screenAwakevalue = '    mScreenOnEarly=true mScreenOnFully=true mOrientationSensorEnabled=false\n'
    allList = os.popen(cmd).readlines()
    if screenAwakevalue in allList:
        return True
    else:
        return False


def isLock(deviceid = ''):
    '''
        判断的依据是'    mAwake=false\n'
        '''
    if deviceid == '':
        cmd = 'adb shell dumpsys window policy'
    else:
        cmd = 'adb -s ' + deviceid + ' shell dumpsys window policy'
    screenAwakevalue = '    mShowingLockscreen=true mShowingDream=false mDreamingLockscreen=true\n'
    allList = os.popen(cmd).readlines()
    if screenAwakevalue in allList:
        return True  # 锁着
    else:
        return False  # 没锁


def sign():
    start_app = f"adb shell am start -n {donyin_package_name}/{douyin_activity_name}"
    if isAwaked():
        if isLock():
            print('unlock')
            os.system(unlock)
        else:
            pass
    else:
        # 唤醒屏幕并解锁
        print('wake up and unlock')
        os.system(wake_up)
        time.sleep(1)
        os.system(unlock)

    print("启动dd")
    os.system(start_app)
    time.sleep(15)
    if isAwaked():
        if isLock():
            os.system(unlock)
        else:
            pass
    else:
        # 唤醒屏幕并解锁
        os.system(wake_up)
        time.sleep(1)
        os.system(unlock)

    # 操作钉钉
    os.system(tap_place_index)
    time.sleep(1)
    os.system(tap_place)
    # 下滑一下 保证位置
    os.system(wrap_a)
    # 收起
    time.sleep(2)
    os.system(shut_up)
    time.sleep(2)
    print('点击')
    os.system(tap_place_kaoqin2)
    # os.system(tap_place_kaoqin)
    # time.sleep(6)
    # os.system(tap_place_daka)
    time.sleep(8)

    if current_time <= "10:30":
        os.system(tap_place_shangban)
        print(1)
        time.sleep(5)
        # 打卡完 返回
        os.system(turnback)
    else:
        if current_time < "20:00":
            os.system(tap_place_xiaban)
            print("下班")
        else:
            os.system(tap_place_xiaban)
            print("点击一次下班保证打了卡")
            time.sleep(3)
            tap_place_gengxin = "adb  shell input tap 115 713"
            tap_place_gengxin_queren = "adb  shell input tap 569 713"
            os.system(tap_place_gengxin)
            print("更新")
            time.sleep(3)
            os.system(tap_place_gengxin_queren)
        time.sleep(5)
        # 打卡完 返回
        os.system(turnback)

    # 退出
    os.system(return_a)
    os.system(return_b)
    os.system(return_ding_index)
    os.system(return_index)



# 获取当前时间 格式20180213
nowTime = time.strftime('%Y%m%d', time.localtime())
date = nowTime
# print(date)
# 节假日接口
server_url = "http://api.goseek.cn/Tools/holiday?date="

vop_url_request = requests.get(server_url + date)

vop_response = vop_url_request.text

vop_data = json.loads(vop_response)
print(vop_data)
# 获取节假日结束

if vop_data['data'] == 1:
    pass  # 法定节假日跳过
else:
    print('不是法定节假日')

    if isAwaked():
        if isLock():
            print('unlock')
            os.system(unlock)
        else:
            print('屏幕没锁')
            pass
    else:
        # 唤醒屏幕并解锁
        print('wake up and unlock2')
        # 唤醒屏幕并解锁
        os.system(wake_up)
        time.sleep(1)
        os.system(unlock)
        time.sleep(1)
        os.system(return_index)

    # 双休打卡
    if mod == 1 and int(current_weekday) in [1, 2, 3, 4, 5]:
        if int(current_weekday) == 5 and current_time < "20:30" and current_time > "10:30":
            sign()  # 打卡
        elif int(current_weekday) in [1, 2, 3, 4] and current_time > "20:30":
            sign()  # 打卡
        elif int(current_weekday) in [1, 2, 3, 4, 5] and current_time < "10:30":
            sign()
        else:
            if current_time > "18:00":
                sign()
            else:
                print('不是周末，打卡太早1')  # 跳过

    # 单休打卡
    elif mod == 0 and int(current_weekday) in [1, 2, 3, 4, 5, 6]:
        if int(current_weekday) == 6 and current_time < "20:30" and current_time > "10:30":
            sign()  # 打下班卡
        elif int(current_weekday) in [1, 2, 3, 4, 5] and current_time > "20:30":
            sign()  # 打下班卡
        elif int(current_weekday) in [1, 2, 3, 4, 5,6] and current_time < "10:30":
            sign()  # 打上班卡
        else:
            if current_time > "18:00":
                sign()
            else:
                print('不是周末，打卡太早_单休')  # 跳过
    else:
        print('未知原因取消打卡')  # 跳过
os.system(kill_dingding)
os.system(start_airdroid)
time.sleep(3)
os.system(wake_up)
time.sleep(3)
exit()
