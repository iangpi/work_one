#coding:utf-8
from selenium import webdriver
import os,time
chromepath=os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
#封装打开、关闭chrome和firefox的方法
class The_Driver(object):
    def the_browser(self,browser_name):
        if browser_name=='ff':
            self.my_browser=webdriver.Firefox()
        if browser_name=='ch':
            self.my_browser=webdriver.Chrome(chromepath)
        return self.my_browser
    def open_browser(self,the_url):
        self.my_browser.get(the_url)
    def close_browser(self):
        self.my_browser.quit()
if __name__=="__main__":
    the_url=r'http://www.baidu.com'
    mytest=The_Driver()
    mytest.the_browser('ff')
    mytest.open_browser(the_url)
    time.sleep(3)
    mytest.close_browser()
    mytest.the_browser('ch')
    mytest.open_browser(the_url)
    time.sleep(3)
    mytest.close_browser()
