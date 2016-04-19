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

class AppCenterTest(unittest.TestCase):
    """数据中心测试类"""
    def setUp(self):
        #实例化MyBase里的Base类
        driver=webdriver.Firefox()
        self.the_dr=Base(driver)
        #实例化LoginPage里的Login类，并登录
        login=Login(driver)
        login.loginpage()
        print ("test start")
    def tearDown(self):
        self.the_dr.quit_browser()
        print ("test end")
    def test_edit_pw_001(self):
        """测试是否到了编辑密码页面"""
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
            print ("assert test_001 fail")
        else:
            pass
    def test_edit_pw_002(self):
        """测试不输入任何东西，修改密码"""
        self.the_dr.open_browser(url_dict['编辑密码url'])
        self.the_dr.by_xpath(Datebase_dict['修改密码按钮_el']).click()
        time.sleep(2)
        get_text=self.the_dr.by_id("oldPassword").text
        hope_text='请填写原密码'
        try:
            assert get_text==hope_text
        except:
            print ("assert test_002 fail")
        else:
            pass
    def test_edit_pw_003(self):
        """不输入新密码确认"""
        self.the_dr.open_browser(url_dict['编辑密码url'])
        self.the_dr.by_xpath(Datebase_dict['输入新密码_el']).send_keys("wxg")
        self.the_dr.by_xpath(Datebase_dict['新密码确认_el']).send_keys("wxg")
        self.the_dr.by_xpath(Datebase_dict['修改密码按钮_el']).click()
        time.sleep(2)
        get_text=self.the_dr.by_id("newPassword").text
        hope_text='请填写原密码'
        try:
            assert get_text==hope_text
        except:
            print ("assert test_003 fail")
        else:
            pass
    def test_edit_pw_004(self):
        """不输入新密码"""
        self.the_dr.open_browser(url_dict['编辑密码url'])
        self.the_dr.by_xpath(Datebase_dict['输入旧密码_el']).send_keys('wxg')
        self.the_dr.by_xpath(Datebase_dict['新密码确认_el']).send_keys('wxg')
        self.the_dr.by_xpath(Datebase_dict['修改密码按钮_el']).click()
        time.sleep(2)
        get_text=self.the_dr.by_id("newPassword").text
        hope_text='请填写新密码'
        try:
            assert get_text==hope_text
        except:
            print ("test 004 fail")
        else:
            pass
    def test_edit_pw_005(self):
        """不输入确认密码"""
        self.the_dr.open_browser(url_dict['编辑密码url'])
        self.the_dr.by_xpath(Datebase_dict['输入旧密码_el']).send_keys('wxg')
        self.the_dr.by_xpath(Datebase_dict['输入新密码_el']).send_keys('wxg')
        self.the_dr.by_xpath(Datebase_dict['修改密码按钮_el']).click()
        time.sleep(2)
        get_text=self.the_dr.by_id("confireNewPassword").text
        hope_text='请填写确认新密码'
        try:
            assert get_text==hope_text
        except:
            print ("test 005 fail")
        else:
            pass
    def test_edit_pw_006(self):
        """新密码和新密码确认不一致"""
        self.the_dr.open_browser(url_dict['编辑密码url'])
        self.the_dr.by_xpath(Datebase_dict['输入旧密码_el']).send_keys('wxg')
        self.the_dr.by_xpath(Datebase_dict['输入新密码_el']).send_keys('wxg')
        self.the_dr.by_xpath(Datebase_dict['新密码确认_el']).send_keys('123')
        self.the_dr.by_xpath(Datebase_dict['修改密码按钮_el']).click()
        time.sleep(2)
        get_text=self.the_dr.by_id("confireNewPassword").text
        hope_text='两次输入的密码不一致'
        try:
            assert get_text==hope_text
        except:
            print ("test 006 fail")
        else:
            pass
    def test_edit_pw_007(self):
        """修改密码成功"""
        self.the_dr.open_browser(url_dict['编辑密码url'])
        self.the_dr.by_xpath(Datebase_dict['输入旧密码_el']).send_keys('wxg')
        self.the_dr.by_xpath(Datebase_dict['输入新密码_el']).send_keys('wxg')
        self.the_dr.by_xpath(Datebase_dict['新密码确认_el']).send_keys('wxg')
        self.the_dr.by_xpath(Datebase_dict['修改密码按钮_el']).click()
        time.sleep(2)
        get_text=self.the_dr.by_xpath(".//*[@id='modifypasswordpost']/div[1]/span").text
        hope_text='密码修改成功'
        try:
            assert get_text==hope_text
        except:
            print ("test 007 fail")
        else:
            pass
if __name__=="__main__":
    unittest.main()
    # testunit=unittest.TestSuite()
    # testunit.addTest(AppCenterTest("test_001_on_page_edit_password"))
    # # 用时间命名文件名标明测试时间
    # test_time=time.strftime("%Y-%m-%d %H_%M_%S")
    # # 家里的存放地址
    # # save_path=os.path.abspath(r"E:\mypython\pengpeng\pp_test_report\testreport")
    # # 公司的存放地址
    # #save_path=os.path.abspath(r'D:\mygit\work_one\v_two\pp_test_report\datebase_testreport')
    # filename='D:\\mygit\\work_one\\v_3\\pp_test_report\\datebase_testreport\\'+test_time+'result.html'
    # fp=file(filename,'wb')
    # runner=HTMLTestRunner(stream=fp,
    #                       title='数据中心测试报告',
    #                       description='设置类子项目测试报告'
    #                       )
    # runner.run(testunit)
    # fp.close()