#coding=utf-8
from selenium.webdriver.common.by import By
from selenium import webdriver
import sys,time,unittest
sys.path.append("\\allpage")
from allpage import login_page


class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login126(self):
        '''正确用户名密码登陆'''
        driver=self.driver
        username='username'
        password='password'
        login_page.test_user_login(driver,username,password)

        '''
        try:
            self.assertEqual(num, 10, msg="login error!!")
        except AssertionError,msg:
            print msg
        '''

    def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
