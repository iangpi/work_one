#coding:utf-8
from appium.webdriver.common.touch_action import TouchAction

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

#联系从屏幕获取坐标后，模拟滑滑动操作
dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(10)
TouchAction(dr).press(x=800,y=1400).move_to(x=-700,y=0).release().perform()
'''
如果你想从坐标(x=800,y=1400)，移动到坐标(x=100,1400)，就是在手机下方从右向左移动。
根据语法表面意思，move_to，后面的坐标，是你想要移动到的地方的坐标，
但是如果你直接写了你想要移动到的坐标，程序是给你做了加法，可以通过appium日志查看到，
如果按照下面的去写，最后传过去的坐标是move_to(900，2800),但是手机屏幕是1080*1920的，
就会报错，说你坐标无效的，因为y坐标已经超出1920的边界了。巨坑无比啊！
所以，第二个坐标，实际不是你想要的位置，而是变化量，
向比自己坐标小的地方移动，就是减法，
向比自己坐标大的地方移动，就是加法。
不移动，变化量就是0，那直接写0就可以了
TouchAction(dr).press(800,1400).move_to(100,1400).release().perform()
'''
time.sleep(10)
dr.quit()