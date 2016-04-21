#coding:utf-8
import os
import time
import unittest
from selenium import webdriver
# from lib2to3.pgen2.driver import Driver
# from lib2to3.tests.support import driver

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)
desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'
desired_caps['browserName']=''
desired_caps['version']='6.0.1'
#这是测试机的型号，可以查看手机的关于本机选项获得
desired_caps['deviceName']='hammerhead'
desired_caps['app'] = PATH(r'D:\test_app\weixin_780.apk')
'''
# 被测试的App在电脑上的位置，如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
# desired_caps['appPackage']='com.subject.zhongchou'
# desired_caps['appActivity']='.ZhongChou'
'''

driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(30)
driver.find_element_by_id('com.tencent.mm:id/akn').send_keys('112233')
time.sleep(3)
driver.find_element_by_id('com.tencent.mm:id/akv').click()
time.sleep(5)
