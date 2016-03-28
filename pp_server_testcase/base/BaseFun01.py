#coding:utf-8
from selenium import webdriver
import sys,os,time
reload(sys)
sys.setdefaultencoding('utf-8')#避免出现乱码
class Base(object):
    def open_browser(self,the_url):
        self.ff=webdriver.Firefox()
        self.ff.refresh()
        self.ff.maximize_window()
        self.ff.get(the_url)
    #封装定位方法
    def by_id(self,the_id):
        return self.ff.find_element_by_id(the_id)
    def by_classname(self,the_classname):
        return self.ff.find_element_by_class_name(the_classname)
    def by_xpath(self,the_xpath):
        return self.ff.find_element_by_xpath(the_xpath)
    #封装用户名和密码输入
    def login(self,u,p):
        self.by_id('username').clear()
        self.by_id('username').send_keys(u)
        self.by_id('password').clear()
        self.by_id('password').send_keys(p)
        self.by_id('submit').click()
        #self.assertEqual('搜索',self.by_xpath(".//*[@id='content']/div/div/div/div[2]/div[2]/div/a").text)
    def close_browser(self):
        self.ff.quit()
if __name__=='__main__':
    mytest=Base()
    mytest.open_browser(r"http://awsbj-openmanagement.xingyunzhi.cn/developer-user/login")
    mytest.login('wxg','wxg')
    el=mytest.by_xpath(".//*[@id='content']/div/div/div/div[2]/div[2]/div/a").text
