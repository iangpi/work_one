#coding:utf-8
from PPMPChoseBrowser import The_Driver
from Variables import the_test_url,the_url,firefox,chrome,chromepath
import time

my_driver=The_Driver()#实例化类
mybrowser=firefox
#封装定位方法
class Find_Element(object):
    def by_id(self,the_id):
        dr=my_driver.the_browser(mybrowser)
        dr.get(the_test_url)
        return dr.find_element_by_id(the_id)

    def by_xpath(self,the_xpath):
        dr=my_driver.the_browser(mybrowser)
        dr.get(the_test_url)
        return dr.find_element_by_xpath(the_xpath)

    def by_classname(self,the_classname):
        dr=my_driver.the_browser(mybrowser)
        dr.get(the_test_url)
        return dr.find_element_by_class_name(the_classname)

if __name__=="__main__":
    mytest=Find_Element()
    mytest.by_id('kw').send_keys('12306')
    mytest.by_id('su').click()

    print a
    # assert the_name==u'把百度设为首页'.encode('gbk').decode('utf-8')
    #
    # time.sleep(3)
    # my_driver.close_browser()
    #
    # mytest.by_xpath(".//*[@id='kw']").send_keys('12306')
    # time.sleep(3)
    # my_driver.close_browser()
    #
    # mytest.by_classname("cp-feedback").click()
    # time.sleep(5)
    # my_driver.close_browser()