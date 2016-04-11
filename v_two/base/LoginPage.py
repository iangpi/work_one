#coding:utf-8
from Page import Base
from selenium import webdriver
import sys
import os
import time
import Variables

#避免出现乱码
reload(sys)
sys.setdefaultencoding('utf-8')
#跨文件引用
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

class Login(object):
    def __init__(self):
        #实例化类
        self.dr=Base(webdriver.Firefox())
        #引入常用变量
        self.url=Variables.the_real_url
        self.el_username=Variables.el_username
        self.el_password=Variables.el_password
        self.el_submit=Variables.el_submit
        self.u=Variables.username
        self.p=Variables.password
    def loginpage(self):
        self.dr.open_browser(self.url)
        self.dr.by_id(self.el_username).clear()
        self.dr.by_id(self.el_username).send_keys(self.u)
        self.dr.by_id(self.el_password).clear()
        self.dr.by_id(self.el_password).send_keys(self.p)
        self.dr.by_id(self.el_submit).click()
        try:
            test_el=self.dr.by_xpath(".//*[@id='content']/div/div/div/div[2]/div[2]/div/a").text
            assert test_el==u'搜索'
        except:
            print 'assert 001 fail'
        else:
            pass
    def closepage(self):
        self.dr.quit_browser()
if __name__=="__main__":
    test001=Login()
    test001.loginpage()
    time.sleep(3)
    test001.closepage()