#coding:utf-8
import sys
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
#跨文件引包
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from base.Variables import Datebase_dict
from base.LoginPage import Login
from base.Page import Base

from selenium import webdriver

class AppCenterTest(unittest.TestCase):
    def begin(self):
        print ("test start")
    def test_on_page_edit_password(self):
        self.test=Login()
        self.test.loginpage()
        the_dr=Base(self.driver)
        the_dr.by_xpath(Datebase_dict['wxg_el']).click()
        the_dr.by_xpath(Datebase_dict['修改密码_el']).click()
        #开始断言
        get_text=the_dr.by_xpath(Datebase_dict['个人信息_el']).text
        hope_text=u'个人信息'
        try:
            assert get_text==hope_text
        except:
            print "assert_0002 fail"
        else:
            pass
    def end(self):
        self.test.closepage()
        print ("test end")
if __name__=="__main__":
    test001=AppCenterTest()
    test001.begin(webdriver.Firefox())
    test001.on_page_edit_password()
    time.sleep(2)
    test001.end()

    # testunit=unittest.TestSuite()
    # testunit.addTest(AppCenterTest("test_on_page_edit_password"))
    # test_time=time.strftime("%Y_%m_%d_%H_%M_%S")
    # #save_path=os.path.abspath(r"E:\mypython\pengpeng\pp_test_report\testreport")#家里的存放地址
    # save_path=os.path.abspath(r"D:\mygit\work_one\v_two\pp_test_report\app_center_report")#公司的存放地址
    # filename=save_path+test_time+'.html'
    # print filename
    # htmlreprot=open(filename,'wb')
    # runner=HTMLTestRunner(stream=htmlreprot,
    #                       title='数据中心',
    #                       description='这是测试报告详细内容'
    #                       )
    # runner.run(testunit)
    # htmlreprot.close()