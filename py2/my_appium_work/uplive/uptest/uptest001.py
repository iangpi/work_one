#coding:utf-8
'''夸app启动，
from appium import webdriver
import os
import time
import sys
sys.path.append('./base')
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'#系统
desired_caps['browserName']=''
# desired_caps['version']='6.0.1'#nexus5的系统版本
# desired_caps['deviceName']='06b947cf00691c51'#这是nexus5的型号，adb devices获得
desired_caps['version']='5.0.2'#红迷note2的系统版本
desired_caps['deviceName']='6LJZW4DUDQCM8L5T'#红迷note2的型号
# 被测试的App在电脑上的位置，如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
desired_caps['appPackage']='com.asiainno.uplive'#uplive的
desired_caps['appActivity']='com.asiainno.uplive.init.splash.SplashActivity'#uplive的
# desired_caps['appPackage']='com.tencent.mm'#weixin
# desired_caps['appActivity']='com.tencent.mm.ui.LauncherUI'#weixin


dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(3)
dr.start_activity('com.asiainno.daidai','com.asiainno.daidai.init.ui.SplashActivity')
'''