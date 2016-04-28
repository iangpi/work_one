#coding:utf-8
from appium import webdriver
import time
import sys

#本文件夹导入包
sys.path.append('./dd_base')
import DD_Data
#引包DD_Data，并实例化类
Data=DD_Data.Data()

#避免出现乱码
reload(sys)
sys.setdefaultencoding('utf-8')

class Base(object):
    def __init__(self,phone_version,phone_name,apk_path):
        self.desired_caps=Data.set_phone(phone_version,phone_name,apk_path)

    def start_driver(self):
        self.dr=webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)
        return self.dr

    def end_driver(self):
        return self.dr.quit()

    def by_id(self,the_id):
        el=self.dr.find_element_by_id(the_id)
        return el

    def by_xpath(self,the_xpath):
        el=self.dr.find_element_by_xpath(the_xpath)
        return el

    def find_id_from_ids(self,the_ids,number):
        el=self.dr.find_elements_by_id(the_ids).pop(number)
        return el

    def find_class_from_classes(self,the_classes,number):
        el=self.dr.find_elements_by_class_name(the_classes).pop(number)
        return el

    def from_to(self,el_a,el_b):#从元素a拖动到元素b
        pass
        i=elements
        a=i.pop(-1)
        a=i.pop(0)
        move=self.dr.drag_and_drop(el_a,el_b)
        return move

if __name__=="__main__":
    version=Data.phone_info('redminote2版本')
    name=Data.phone_info('redminote2设备名')
    apk_path=r'D:\test_app\daidai_2016.04.15_1.0.0_1040.production_yzl.apk'

    test001=Base(version,name,apk_path)
    test001.start_driver()
    time.sleep(2)
    test001.end_driver()
