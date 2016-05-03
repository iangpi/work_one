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
        print ('test start')
        self.driver=browsers['ff']
        self.the_dr=Base(self.driver)
        #实例化MyBase里的Login类，并登录
        login=Login(self.driver)
        login.loginpage()
        self.driver.implicitly_wait(15)
    def tearDown(self):
        self.the_dr.quit_browser()
        print ('test end')
    def test_001(self):
        pass
if __name__=="___main_":
    unittest.main()