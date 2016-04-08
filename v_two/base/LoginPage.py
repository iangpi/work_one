#coding:utf-8
from Page import Base
from selenium import webdriver
import sys
import os
import time
import Variables

#避免出现乱码
reload(sys)
sys.setdefaultencoding('utf-8')
#跨文件引用
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

class Login(object):
    #成功登录方法
    def loginpage(self):
        #实例化类
        dr=Base(webdriver.Firefox())
        url=Variables.the_real_url
        #引入常用变量
        el_username=Variables.el_username
        el_password=Variables.el_password
        el_submit=Variables.el_submit
        u=Variables.username
        p=Variables.password

        dr.open_browser(url)
        dr.by_id(el_username).clear()
        dr.by_id(el_username).send_keys(u)
        dr.by_id(el_password).clear()
        dr.by_id(el_password).send_keys(p)
        dr.by_id(el_submit).click()
        try:
            test_el=dr.by_xpath(".//*[@id='content']/div/div/div/div[2]/div[2]/div/a").text
            assert test_el==u'搜索'
        except:
            print 'assert 001 fail'
        else:
            print 'assert 001 pass'
        # time.sleep(3)
        # dr.quit_browser()

if __name__=="__main__":
    test001=Login()
    test001.loginpage()