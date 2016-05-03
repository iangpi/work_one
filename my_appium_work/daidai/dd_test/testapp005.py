#coding:utf-8
#给手手机快速装app的方法
from appium import webdriver
import os
import sys
sys.path.append('./base')
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'#系统
desired_caps['browserName']=''
desired_caps['version']='6.0.1'
desired_caps['deviceName']='0a609382'
desired_caps['app'] = PATH(r'E:\daidai_2016.04.15_1.0.0_1040.production_yzl.apk')

#联系从屏幕获取坐标后，模拟滑滑动操作
dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)