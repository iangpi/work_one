#coding:utf-8
import sys
import time
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf-8')#避免出现乱码
sys.path.append('./base')
from Variables import url_dict
from Variables import login_el
from Variables import u_p
from Variables import Datebase_dict
class Base(object):
    #初始化浏览器驱动
    def __init__(self,driver):
        self.driver=driver
    #打开浏览器
    def open_browser(self,url):
        self.driver.get(url)
    #关闭浏览器
    def quit_browser(self):
        self.driver.quit()
    #定位器
    def by_id(self,the_id):
        el=self.driver.find_element_by_id(the_id)
        return el
    def by_xpath(self,the_xpath):
        el=self.driver.find_element_by_xpath(the_xpath)
        return el
    def by_class_name(self,the_class_name):
        el=self.driver.find_element_by_class_name(the_class_name)
        return el
class Login(Base):
    def loginpage(self):
        self.mybase=Base(self.driver)
        self.mybase.open_browser(url_dict['登录url'])
        self.mybase.by_id(login_el['用户名el']).clear()
        self.mybase.by_id(login_el['用户名el']).send_keys(u_p['用户名'])
        self.mybase.by_id(login_el['密码el']).clear()
        self.mybase.by_id(login_el['密码el']).send_keys(u_p['密码'])
        self.mybase.by_id(login_el['登录按钮el']).click()
        try:
            test_el=self.mybase.by_xpath(Datebase_dict['搜索按钮_el']).text
            assert test_el==u'搜索'
        except:
            print 'assert 0001 fail'
        else:
            pass
if __name__=='__main__':
    #实例Base化类
    test001=Base(webdriver.Firefox())
    #引用常用变量的文件
    url=url_dict['百度测试用url']

    test001.open_browser(url)
    test001.by_id('kw').send_keys('123')
    time.sleep(2)

    test001.by_xpath(".//*[@id='kw']").clear()
    test001.by_xpath(".//*[@id='kw']").send_keys('456')
    time.sleep(2)

    test001.by_class_name("s_ipt").clear()
    test001.by_class_name("s_ipt").send_keys('789')
    time.sleep(2)
    test001.quit_browser()

    #实例化Login类
    test002=Login(webdriver.Firefox())
    test002.loginpage()
    time.sleep(2)
    test002.quit_browser()