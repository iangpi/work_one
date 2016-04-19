#coding:utf-8
import sys
import os
import time
from selenium import webdriver
#跨文件引包
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from base.Variables import url_dict
from base.MyBase_v1 import Base
from base.MyBase_v1 import Login


class All_Page_App_Center(object):
    def __init__(self,driver):
        #实例化MyBase_v1中的Base类
        self.the_dr=Base(driver)
        login=Login(driver)
        login.loginpage()
    def page_edit_password(self):
        return self.the_dr.open_browser(url_dict['编辑密码url'])
    def page_user_list(self):
        return self.the_dr.open_browser(url_dict['用户列表url'])
    def page_company_list(self):
        return self.the_dr.open_browser(url_dict['公司列表url'])
if __name__=="__main__":
    test001=All_Page_App_Center(webdriver.Firefox())

    test001.page_edit_password()
    time.sleep(2)

    test001.page_user_list()
    time.sleep(2)

    test001.page_company_list()
    time.sleep(2)
    test001.the_dr.quit_browser()