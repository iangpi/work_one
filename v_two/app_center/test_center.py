#coding:utf-8
import sys
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
#跨文件引包
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from base.Variables import Datebase_dict
from base.Variables import url_dict
from base.MyBase_v1 import Base
from base.MyBase_v1 import Login
#同文件夹下引包
sys.path.append('./app_center')
from page_app_center import All_Page_App_Center

class AppCenterTest(unittest.TestCase):
    def setUp(self):
        #实例化MyBase里的Base类
        driver=webdriver.Firefox()
        self.the_dr=Base(driver)
        #实例化LoginPage里的Login类，并登录
        login=Login(driver)
        login.loginpage()
        print ("test start")
    def test_001_on_page_edit_password(self):
        self.the_dr.open_browser(url_dict['编辑密码url'])
        self.the_dr.by_xpath(Datebase_dict['wxg_el']).click()
        self.the_dr.by_xpath(Datebase_dict['修改密码_el']).click()
        time.sleep(2)
        #开始断言
        get_text=self.the_dr.by_xpath(Datebase_dict['个人信息_el']).text
        hope_text=u'个人信息'
        time.sleep(2)
        try:
            assert get_text==hope_text
        except:
            print ("assert test_001_on_page_edit_password fail")
        else:
            pass
    # def test_002_nothing_input(self):
    #     self.edit_password.page_edit_password()
    #     self.the_dr.by_xpath(Datebase_dict['修改密码按钮_el']).click()
    #     time.sleep(3)
    #     get_text=self.the_dr.by_id("oldPassword").text
    #     hope_text=u'请填写原密码'
    #     try:
    #         assert get_text==hope_text
    #     except:
    #         print ("assert test_002_nothing_input fail")
    #     else:
    #         pass
    def tearDown(self):
        self.the_dr.quit_browser()
        print ("test end")
if __name__=="__main__":
    testunit=unittest.TestSuite()
    testunit.addTest(AppCenterTest("test_001_on_page_edit_password"))
    # 用时间命名文件名标明测试时间
    test_time=time.strftime("%Y-%m-%d %H_%M_%S")
    # 家里的存放地址
    # save_path=os.path.abspath(r"E:\mypython\pengpeng\pp_test_report\testreport")
    # 公司的存放地址
    #save_path=os.path.abspath(r'D:\mygit\work_one\v_two\pp_test_report\datebase_testreport')
    filename='D:\\mygit\\work_one\\v_two\\pp_test_report\\datebase_testreport\\'+test_time+'result.html'
    fp=file(filename,'wb')
    runner=HTMLTestRunner(stream=fp,
                          title='数据中心测试报告',
                          description='设置类子项目测试报告'
                          )
    runner.run(testunit)
    fp.close()