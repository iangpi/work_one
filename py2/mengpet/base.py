#coding:utf-8
from selenium import webdriver
import unittest,time
ff=webdriver.Firefox()
class mengpetbase(unittest.TestCase):
    def setUp(self,the_url):
        self.ff=webdriver.Firefox()
        self.ff.get(the_url)
        self.ff.set_window_size(600,500)
    def tearDown(self):
        self.ff=webdriver.Firefox()
        time.sleep(2)
        self.ff.quit()
    def by_id(self,the_id):
        return self.ff.find_element_by_id(the_id)
    def by_xpath(self,the_xpath):
        return self.ff.find_element_by_xpath(the_xpath)

if __name__=="__main__":
    unittest.main