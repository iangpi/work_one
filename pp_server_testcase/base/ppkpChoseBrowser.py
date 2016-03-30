#coding:utf-8
from selenium import webdriver
import os,time
#封装使用不同浏览器的方法
class Chose_Browser(object):
    def which_Browser(self,br_name):
        chromepath=os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        if br_name=='firefox':
            self.driver=webdriver.Firefox()
        elif br_name=='chrome':
            self.driver=webdriver.Chrome(chromepath)
        else:
            raise Exception(TypeError)
        return self.driver
    def open_Browser(self,the_url):
        the_browser=self.which_Browser(br_name='')
        the_browser.get(the_url)
    def close_Browser(self):
        the_browser=self.which_Browser(br_name='')
        the_browser.quit()
if __name__=="__main__":
    testbrowser=Chose_Browser()
    testbrowser.which_Browser('firefox')
    testbrowser.open_Browser(r'http://www.baidu.com')
    time.sleep(3)
    testbrowser.close_Browser()