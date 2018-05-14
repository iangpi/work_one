#coding:utf-8
from appium import webdriver
import os
import time

class Data(object):
    def set_phone(self,phone_version,phone_deviceName,apk_path):
        desired_caps={'device':'android',
                      'platformName':'Android',
                      'browserName':'',
                      'version':phone_version,#系统版本
                      'deviceName':phone_deviceName,#设备物理名字，adb devices获得
                      'app':os.path.abspath(apk_path)#apk在pc上的绝对地址
                      }
        return desired_caps#返回了所需的配置信息

    def phone_info(self,info):
        infos_dict={'nexus5版本':'6.0.1',
                    'nexus5设备名':'06b947cf00691c51',
                    'redminote2版本':'5.0.2',
                    'redminote2设备名':'6LJZW4DUDQCM8L5T',
                    'nexus6版本':'6.0.1',
                    'nexus6设备名':'ZY222ZG98P',
                    'nexus7版本':'6.0.1',
                    'nexus7设备名':'0a609382',
                    '红米1版本':'4.2.1',
                    '红迷1设备名':'UW6SB69SHANVKRGU'
                    }
        return infos_dict[info]

    def home_els(self,name):
        els={
            '商店':'com.asiainno.daidai:id/shop',
            '查找':'com.asiainno.daidai:id/search',
            '设置':'com.asiainno.daidai:id/setting',
            '头像':'com.asiainno.daidai:id/iv_header_icon',
            '聊天':"//android.support.v7.app.a$f[@index='0']",
            '好友':"//android.support.v7.app.a$f[@index='1']"
            }
        return els[name]

if __name__=="__main__":
    test001=Data()

    version=test001.phone_info('redminote2版本')
    name=test001.phone_info('redminote2设备名')
    apk_path=r'D:\test_app\daidai_2016.04.15_1.0.0_1040.production_yzl.apk'
    shop=test001.home_els('商店')

    desired_caps=test001.set_phone(version,name,apk_path)
    dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    dr.find_element_by_id(shop).click()
    time.sleep(2)
    dr.keyevent(4)
    time.sleep(2)
    dr.quit()
    package tutorial;