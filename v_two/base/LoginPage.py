#coding:utf-8
from Page import Base
from selenium import webdriver
import sys
import time

from Variables import url_dict
from Variables import login_el
from Variables import u_p
from Variables import Datebase_dict
#避免出现乱码
reload(sys)
sys.setdefaultencoding('utf-8')
#本文件夹内引用Variables包
sys.path.append('./base')
class Login(object):
    def __init__(self,driver):
        #实例化类，传参浏览器驱动
        self.dr=Base(driver)
    def loginpage(self):
        self.dr.open_browser(url_dict['登录url'])
        self.dr.by_id(login_el['用户名el']).clear()
        self.dr.by_id(login_el['用户名el']).send_keys(u_p['用户名'])
        self.dr.by_id(login_el['密码el']).clear()
        self.dr.by_id(login_el['密码el']).send_keys(u_p['密码'])
        self.dr.by_id(login_el['登录按钮el']).click()
        try:
            test_el=self.dr.by_xpath(Datebase_dict['搜索按钮_el']).text
            assert test_el==u'搜索'
        except:
            print 'assert 0001 fail'
        else:
            pass
    def closepage(self):
        self.dr.quit_browser()
if __name__=="__main__":
    test001=Login()
    test001.loginpage()
    print ('登录成功')
    time.sleep(3)
    test001.closepage()