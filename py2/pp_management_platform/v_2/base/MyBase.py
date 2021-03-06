#coding:utf-8
import sys
import time
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf-8')#避免出现乱码
sys.path.append('./base')
from Variables import url_dict
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
if __name__=='__main__':
    #实例化类
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