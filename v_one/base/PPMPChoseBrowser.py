#coding:utf-8
from selenium import webdriver
import os,time
from Variables import the_test_url,firefox,chrome
chromepath=os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
#封装打开、关闭chrome和firefox的方法
class The_Driver(object):
    def the_browser(self,input_browser_name):
        if input_browser_name=='ff':
            self.my_browser=webdriver.Firefox()
        if input_browser_name=='ch':
            self.my_browser=webdriver.Chrome(chromepath)
        return self.my_browser
    def open_browser(self,input_url):
        self.my_browser.get(input_url)
    def close_browser(self):
        self.my_browser.quit()
if __name__=="__main__":
    mytest=The_Driver()#实例化

    #测试用firefox打开
    mytest.the_browser(firefox)
    mytest.open_browser(the_test_url)
    time.sleep(3)
    mytest.close_browser()

    #测试用chrome打开
    mytest.the_browser(chrome)
    mytest.open_browser(the_test_url)
    time.sleep(3)
    mytest.close_browser()
