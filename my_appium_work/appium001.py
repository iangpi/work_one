#coding:utf-8
import os
import time
# import unittest
from appium import webdriver

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'#系统
desired_caps['browserName']=''
desired_caps['version']='6.0.1'#系统版本
desired_caps['deviceName']='hammerhead'#这是测试机的型号，可以查看手机的关于本机选项获得
desired_caps['app'] = PATH(r'D:\test_app\daidai_2016.04.15_1.0.0_1040.production_yzl.apk')
'''
# 被测试的App在电脑上的位置，如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
# desired_caps['appPackage']='com.subject.zhongchou'
# desired_caps['appActivity']='.ZhongChou'
'''

dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(3)
dr.find_element_by_id('com.asiainno.daidai:id/setting').click()
time.sleep(5)
dr.keyevent(4)
time.sleep(4)
dr.quit()