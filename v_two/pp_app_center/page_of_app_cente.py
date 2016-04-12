#coding:utf-8
import sys
import os
import time
from selenium import webdriver
#跨文件引包
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from base import Variables
from base.LoginPage import Login
from base.Page import Base


class All_Page_App_Center(object):
    def __init__(self,driver):
        #引用LoginPage.py中启动浏览器的方法
        self.test=Login(driver)
        #调用登录方法
        self.test.loginpage()
        #实例化page.py中的Base类
        self.the_dr=Base(driver)
        print ("test start")
    def page_edit_password(self):
        return self.the_dr.open_browser(Variables.edit_password_url)
    def page_account_list(self):
        return self.the_dr.open_browser(Variables.account_list_url)
    def page_company_list(self):
        return self.the_dr.open_browser(Variables.company_list_url)
    def quit(self):
        #引用LoginPage.py中的关闭浏览器方法
        self.test.closepage()
        print ("test end")
if __name__=="__main__":
    test001=All_Page_App_Center(webdriver.Firefox())

    test001.page_edit_password()
    time.sleep(3)

    test001.page_account_list()
    time.sleep(3)

    test001.page_company_list()
    time.sleep(3)
    test001.quit()