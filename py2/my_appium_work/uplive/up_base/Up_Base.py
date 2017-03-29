#coding:utf-8
from appium.webdriver.common.touch_action import TouchAction
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

    def find_ids(self,the_ids):
        els=self.dr.find_elements_by_id(the_ids)
        return els

    def find_classes(self,the_classes):
        els=self.dr.find_elements_by_class_name(the_classes)
        return els

    def from_icon_to_icon(self,elements,a,b):
        '''从一组元素中定位a和b，然后把元素b拖动到a的位置，完成多个元素无法显示完全，通过拖动，挨个遍历所有元素的方法'''
        move=self.dr.drag_and_drop(elements.pop(a),elements.pop(b))
        return move

    def move_to(self,a,b,a1,b1):
        '''
        TouchAction(dr).press(800,1400).move_to(100,1400).release().perform()
        如果你想从坐标(x=800,y=1400)，移动到坐标(x=100,1400)，就是在手机下方从右向左移动。
        根据语法表面意思，move_to，后面的坐标，是你想要移动“到”！！！的地方的坐标，
        但是如果你直接写了你想要移动到的坐标，程序是给你做了加法，可以通过appium日志查看到，
        如果按照上面注释里去写，在日志里你会看到，最后传过去的坐标是move_to(900，2800),也就是他把你传入的2个坐标给相加了！！
        因为是手机屏幕是1080*1920的，就会报错，说你坐标无效的，因为y的最后输出坐标：——2800已经超出1920的边界了。巨坑无比啊！
        所以，第二个坐标，实际不是你想要的位置，而是变化量，并且变化量可以是负数。
        本着社会主义接班人的觉悟，我重新写了这个方法，如下，亲测可用，真正填写你想move_to——也就是移动“到”的地方的坐标
        '''
        return TouchAction(self.dr).press(x=int(a),y=int(b)).move_to(x=int(a1)-int(a),y=int(b1)-int(b)).release().perform()

if __name__=="__main__":
    version=Data.phone_info('nexus7版本')
    name=Data.phone_info('nexus7设备名')
    apk_path=r'E:\daidai_2016.04.15_1.0.0_1040.production_yzl.apk'

    test001=Base(version,name,apk_path)
    test001.start_driver()
    time.sleep(4)
    test001.move_to(500,1400,500,200)
    time.sleep(4)
    test001.by_id(Data.home_els('商店')).click()
    time.sleep(5)
    menu_x=test001.find_classes('android.support.v7.app.a$f')
    time.sleep(5)
    test001.from_icon_to_icon(menu_x,4,0)
    time.sleep(2)
    test001.end_driver()