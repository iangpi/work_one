#coding:utf-8
import sys
import time
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf-8')#避免出现乱码
sys.path.append('./base')
from Variables import base_url
from Variables import login_el
from Variables import u_p
from Variables import apply_center_page
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
        mybase=Base(self.driver)
        mybase.open_browser(base_url['登录url'])
        mybase.by_id(login_el['用户名el']).clear()
        mybase.by_id(login_el['用户名el']).send_keys(u_p['用户名'])
        mybase.by_id(login_el['密码el']).clear()
        mybase.by_id(login_el['密码el']).send_keys(u_p['密码'])
        mybase.by_id(login_el['登录按钮el']).click()
        try:
            get_text=mybase.by_xpath(apply_center_page['搜索按钮_el']).text
            hope_text='搜索'
            assert get_text==hope_text
        except:
            print 'assert 0001 fail'
        else:
            pass
if __name__=='__main__':
    #实例Base化类
    the_dr=Base(webdriver.Firefox())
    #引用常用变量的文件
    url=base_url['百度测试用url']

    the_dr.open_browser(url)
    time.sleep(2)

    the_dr.by_id('kw').send_keys('123')
    time.sleep(2)

    the_dr.by_xpath(".//*[@id='kw']").clear()
    the_dr.by_xpath(".//*[@id='kw']").send_keys('456')
    time.sleep(2)

    the_dr.by_class_name("s_ipt").clear()
    the_dr.by_class_name("s_ipt").send_keys('789')
    time.sleep(2)
    the_dr.quit_browser()

    #实例化Login类
    the_dr001=Login(webdriver.Firefox())
    the_dr001.loginpage()
    time.sleep(2)
    the_dr001.quit_browser()