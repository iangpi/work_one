#coding:utf-8
import unittest
import time
import sys
sys.path.append('./base')
from Variables import browsers
from MyBase import Login
from MyBase import Base

class My_setup_teardown(unittest.TestCase):
    def setUp(self):
        print ("test start")
        #实例化MyBase里的Base类
        driver=browsers['ff']
        self.the_dr=Base(driver)
        #实例化LoginPage里的Login类，并登录
        login=Login(driver)
        login.loginpage()
    def tearDown(self):
        self.the_dr.quit_browser()
        print ("test end")
if __name__=="___main_":
    unittest.main()