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
from base.Variables import login_el
from base.Variables import base_url
from base.Variables import base_page
from base.Variables import set_page
from base.Variables import u_p
from base.MyBase import Base
from base.MyBase import Login

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
    def test_001_edit_pw(self):
        """测试是否到了编辑密码页面"""
        self.the_dr.open_browser(base_url['编辑密码url'])
        self.the_dr.by_xpath(base_page['wxg_el']).click()
        self.the_dr.by_xpath(base_page['修改密码_el']).click()
        time.sleep(1)
        #开始断言
        get_text=self.the_dr.by_xpath(set_page['个人信息_el']).text
        hope_text='1个人信息'
        time.sleep(1)
        self.assertEqual(get_text,hope_text)
        # try:
        #     assert get_text==hope_text
        # except:
        #     print ("assert test_001 fail")
        # else:
        #     pass
    def test_002_edit_pw(self):
        """测试不输入任何东西，修改密码"""
        self.the_dr.open_browser(base_url['编辑密码url'])
        self.the_dr.by_xpath(set_page['修改密码按钮_el']).click()
        time.sleep(1)
        get_text=self.the_dr.by_id("oldPassword").text
        hope_text='请填写原密码'
        self.assertEqual(get_text,hope_text)
    def test_003_edit_pw(self):
        """不输入旧密码"""
        self.the_dr.open_browser(base_url['编辑密码url'])
        self.the_dr.by_xpath(set_page['输入新密码_el']).send_keys(u_p['密码'])
        self.the_dr.by_xpath(set_page['新密码确认_el']).send_keys(u_p['密码'])
        self.the_dr.by_xpath(set_page['修改密码按钮_el']).click()
        time.sleep(2)
        get_text=self.the_dr.by_id("oldPassword").text
        hope_text='请填写原密码'
        # print 'get is'+get_text,'hope is'+hope_text
        self.assertEqual(get_text,hope_text)
    def test_004_edit_pw(self):
        """不输入新密码"""
        self.the_dr.open_browser(base_url['编辑密码url'])
        self.the_dr.by_xpath(set_page['输入旧密码_el']).send_keys(u_p['密码'])
        self.the_dr.by_xpath(set_page['新密码确认_el']).send_keys(u_p['密码'])
        self.the_dr.by_xpath(set_page['修改密码按钮_el']).click()
        time.sleep(2)
        get_text=self.the_dr.by_id("newPassword").text
        hope_text='请填写新密码'
        self.assertEqual(get_text,hope_text)
    def test_005_edit_pw(self):
        """不输入确认密码"""
        self.the_dr.open_browser(base_url['编辑密码url'])
        self.the_dr.by_xpath(set_page['输入旧密码_el']).send_keys(u_p['密码'])
        self.the_dr.by_xpath(set_page['输入新密码_el']).send_keys(u_p['密码'])
        self.the_dr.by_xpath(set_page['修改密码按钮_el']).click()
        time.sleep(2)
        get_text=self.the_dr.by_id("confireNewPassword").text
        hope_text='请填写确认新密码'
        self.assertEqual(get_text,hope_text)
    def test_006_edit_pw(self):
        """新密码和新密码确认不一致"""
        self.the_dr.open_browser(base_url['编辑密码url'])
        self.the_dr.by_xpath(set_page['输入旧密码_el']).send_keys(u_p['密码'])
        self.the_dr.by_xpath(set_page['输入新密码_el']).send_keys(u_p['密码'])
        self.the_dr.by_xpath(set_page['新密码确认_el']).send_keys('123')
        self.the_dr.by_xpath(set_page['修改密码按钮_el']).click()
        time.sleep(2)
        get_text=self.the_dr.by_id("confireNewPassword").text
        hope_text='两次输入的密码不一致'
        self.assertEqual(get_text,hope_text)
    def test_007_edit_pw(self):
        """修改密码成功"""
        self.the_dr.open_browser(base_url['编辑密码url'])
        self.the_dr.by_xpath(set_page['输入旧密码_el']).send_keys(u_p['密码'])
        self.the_dr.by_xpath(set_page['输入新密码_el']).send_keys(u_p['密码'])
        self.the_dr.by_xpath(set_page['新密码确认_el']).send_keys(u_p['密码'])
        self.the_dr.by_xpath(set_page['修改密码按钮_el']).click()
        time.sleep(2)
        get_text=self.the_dr.by_xpath(".//*[@id='modifypasswordpost']/div[1]/span").text
        hope_text='密码修改成功'
        self.assertEqual(get_text,hope_text)
    def test_008_quit(self):
        """退出帐号"""
        self.the_dr.by_xpath(base_page['wxg_el']).click()
        self.the_dr.by_xpath(base_page['退出_el']).click()
        time.sleep(1)
        #获取了推出后，返回会登录页的title
        get_text=self.the_dr.by_id(login_el['登录按钮el']).text
        hope_text='登陆'
        self.assertEqual(get_text,hope_text)
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