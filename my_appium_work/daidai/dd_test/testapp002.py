#coding:utf-8
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
desired_caps['app'] = PATH(r'D:\test_app\daidai_2016.04.15_1.0.0_1040.production_yzl.apk')


dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(2)
dr.find_element_by_id('com.asiainno.daidai:id/shop').click()
time.sleep(2)
all_menu=dr.find_elements_by_class_name("android.support.v7.app.a$f")
time.sleep(2)
print len(all_menu)
hear=all_menu.pop(4)
base=all_menu.pop(0)
dr.drag_and_drop(hear,base)
all_menu1=dr.find_elements_by_class_name("android.support.v7.app.a$f")
all_menu.pop(0).click()
time.sleep(2)
dr.quit()