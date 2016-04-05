#coding:utf-8
from PPMPChoseBrowser import The_Driver
import time
browser_name='ff'
the_url=r"http://www.baidu.com"
my_driver=The_Driver()#实例化类
#封装定位方法
class Find_Element(object):
    def by_id(self,the_id):
        dr=my_driver.the_browser(browser_name)
        dr.get(the_url)
        return dr.find_element_by_id(the_id)

    def by_xpath(self,the_xpath):
        dr=my_driver.the_browser(browser_name)
        dr.get(the_url)
        return dr.find_element_by_xpath(the_xpath)

    def by_classname(self,the_classname):
        dr=my_driver.the_browser(browser_name)
        dr.get(the_url)
        return dr.find_element_by_class_name(the_classname)

if __name__=="__main__":
    mytest=Find_Element()
    mytest.by_id('kw').send_keys('12306')
    time.sleep(3)
    my_driver.close_browser()

    mytest.by_xpath(".//*[@id='kw']").send_keys('12306')
    time.sleep(3)
    my_driver.close_browser()

    mytest.by_classname("cp-feedback").click()
    time.sleep(5)
    my_driver.close_browser()