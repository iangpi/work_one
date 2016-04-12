#coding:utf-8
import sys
import os
import time
import unittest
#跨文件引包
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from base.LoginPage import Login
from base.Page import Base
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class AppCenterTest(object):

    def setUp(self,driver):
        print ("test start")
        self.driver=driver
        self.test=Login(driver)
        self.test.loginpage()
    def test_on_page_edit_password(self):
        the_dr=Base(self.driver)
        the_dr.by_xpath("html/body/div[1]/div/div/button").click()
        the_dr.by_xpath("html/body/div[1]/div/div/ul/li[1]/a").click()
        real_text=the_dr.by_xpath(".//*[@id='content']/div/div/div/div/div/h2").text
        hope_text=u'修改密码'
        try:
            assert real_text==hope_text
        except:
            print "assert_0002 fail"
        else:
            pass
    def test_no_old_password(self):
        """没有输入旧密码提示"""

    def tearDown(self):
        self.test.closepage()
        print ("test end")
if __name__=="__main__":
    test001=AppCenterTest()
    test001.setUp(webdriver.Firefox())
    test001.test_on_page_edit_password()
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