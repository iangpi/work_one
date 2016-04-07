#coding:utf-8
import Variables
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')#避免出现乱码

class Base(object):
    #初始化浏览器驱动
    def __init__(self):
        self.driver=Variables.selenium_driver
    #打开浏览器
    def open(self,url):
        self.driver.get(url)
    #关闭浏览器
    def close(self):
        self.driver.quit()
    #id定位
    def by_id(self,the_id):
        el=self.driver.find_element_by_id(the_id)
        return el
    #xpath定位
    def by_xpath(self,the_xpath):
        el=self.driver.find_element_by_xpath(the_xpath)
        return el
    #classname定位
    def by_classname(self,the_classname):
        el=self.driver.find_element_by_class_name(the_classname)
        return el
if __name__=='__main__':
    #实例化类
    test001=Base()
    #引用常用变量的文件
    test_url=Variables.the_baidu_url
    test001.open(test_url)
    test001.by_id('kw').send_keys('123')
    time.sleep(2)

    test001.by_xpath(".//*[@id='kw']").clear()
    test001.by_xpath(".//*[@id='kw']").send_keys('456')
    time.sleep(2)

    test001.by_classname("s_ipt").clear()
    test001.by_classname("s_ipt").send_keys('789')
    time.sleep(2)

    test001.close()
