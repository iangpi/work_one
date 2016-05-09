#coding:utf-8
#快速获取uid
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
# desired_caps['version']='5.0.2'#红迷note2的系统版本
# desired_caps['deviceName']='6LJZW4DUDQCM8L5T'#红迷note2的型号
desired_caps['app'] = PATH('D:\test_app\up_2016.05.08_1.0.0_667.production_localDevelop.apk')

#联系从屏幕获取坐标后，模拟滑滑动操作
dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
