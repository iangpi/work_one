#coding:utf-8
#appium
from selenium import webdriver
import time
ff=webdriver.Firefox()
ff.get("http://www.baidu.com")
ff.maximize_window()
get_text=ff.find_element_by_xpath(".//*[@id='u1']/a[1]").text
hope_text=u'糯米'
print get_text
print hope_text

assert get_text==hope_text
time.sleep(3)
ff.quit()