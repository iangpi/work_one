#coding:utf-8
import sys
import os
import time
#跨文件引用

parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from base.LoginPage import Login
class BasePage():
    def app_center(self):
        loginsuccess=Login()
        return loginsuccess.loginpage()

if __name__=="__main__":
    test001=BasePage()
    test001.app_center()