#coding:utf-8
from appium import webdriver
from selenium import webdriver
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
desired_caps['app'] = PATH(r'D:\test_app\daidai_2016.04.15_1.0.0_1040.production_yzl.apk')
'''
# 被测试的App在电脑上的位置，如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
# desired_caps['appPackage']='com.asiainno.daidai'
# desired_caps['appActivity']='.ZhongChou'
'''

dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(2)
dr.find_element_by_id('com.asiainno.daidai:id/shop').click()
time.sleep(2)
all_menu=dr.find_elements_by_class_name("android.support.v7.app.a$f")
time.sleep(2)
print len(all_menu)
all_menu.pop(2).click()
time.sleep(2)
all_hear=dr.find_elements_by_id('com.asiainno.daidai:id/llContent')
print len(all_hear)
dr.keyevent(4)#系统返回按钮
time.sleep(2)
dr.quit()