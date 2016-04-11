#coding:utf-8
import sys
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
#跨文件引用
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from base.LoginPage import Login
from base.Page import Base

class AppCenterTest(object):
    def setUp(self,driver):
        print ("test start")
        self.driver=driver
        self.test=Login(driver)
        self.test.loginpage()

    def test_login_add_apk_bak(self):
        find_el=Base(self.driver)
        test=find_el.by_xpath(".//*[@id='content']/div/div/div/div[2]/div[2]/div/a").text
        print test

    def tearDown(self):
        self.test.closepage()
        print ("test end")


if __name__=="__main__":
    test001=AppCenterTest()
    test001.setUp(webdriver.Firefox())
    test001.test_login_add_apk_bak()
    test001.tearDown()



    # testunit=unittest.TestSuite()
    # testunit.addTest(BasePage("test_login_add_apk_bak"))
    # test_time=time.strftime("%Y_%m_%d_%H_%M_%S")
    # save_path=os.path.abspath(r"D:\mygit\work_one\pp_test_report\testreport")#公司的存放地址
    # filename=save_path+test_time+'.html'
    # print filename
    # htmlreprot=open(filename,'wb')
    # runner=HTMLTestRunner(stream=htmlreprot,
    #                       title='这是标题',
    #                       description='这是测试报告详细内容'
    #                       )
    # runner.run(testunit)
    # htmlreprot.close()