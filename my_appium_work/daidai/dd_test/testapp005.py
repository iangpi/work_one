#coding:utf-8
#给手手机快速装app的方法
from appium import webdriver
import os
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'#系统
desired_caps['browserName']=''
desired_caps['version']='4.2.1'
desired_caps['deviceName']='UW6SB69SHANVKRGU'
desired_caps['app'] = PATH(r'D:\test_app\up.apk')

#联系从屏幕获取坐标后，模拟滑滑动操作
dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)