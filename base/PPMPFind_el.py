#coding:utf-8
from PPMPChoseBrowser import The_Driver
import time
#封装定位方法
my_driver=The_Driver()#实例化类，浏览器的选择
class Find_Element(object):
    def by_id(self,the_id,browser_name,the_url):
        dr=my_driver.the_browser(browser_name)
        dr.get(the_url)
        return dr.find_element_by_id(the_id)

    def by_xpath(self,the_xpath,browser_name,the_url):
        dr=my_driver.the_browser(browser_name)
        dr.get(the_url)
        return dr.find_element_by_xpath(the_xpath)

    def by_classname(self,the_classname,browser_name,the_url):
        dr=my_driver.the_browser(browser_name)
        dr.get(the_url)
        return dr.find_element_by_class_name(the_classname)
if __name__=="__main__":
    mytest=Find_Element()
    mytest.by_id('kw','ff',r'http://www.baidu.com').send_keys('12306')
    time.sleep(3)
    my_driver.close_browser()

    mytest.by_xpath(".//*[@id='kw']",'ff',r'http://www.baidu.com').send_keys('12306')
    time.sleep(3)
    my_driver.close_browser()

    mytest.by_classname("cp-feedback",'ff',r'http://www.baidu.com').click()
    time.sleep(5)
    my_driver.close_browser()