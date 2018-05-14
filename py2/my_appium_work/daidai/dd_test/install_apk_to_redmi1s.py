#coding:utf-8
#给手手机快速装app的方法
from appium import webdriver
import os
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'#系统
desired_caps['browserName']=''
desired_caps['version']='6.1.0'
#desired_caps['deviceName']='UW6SB69SHANVKRGU'
#desired_caps['deviceName']='UW6SB69SHANVKRGU'
desired_caps['deviceName']='U20AVCP923DYF'#魅族手机的devicename
desired_caps['app'] = PATH(r'C:\Users\ppldc\Desktop\upLive-domestic-up-localDevelop-debug.apk')

#启动
dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
dr.set_network_connection(4)