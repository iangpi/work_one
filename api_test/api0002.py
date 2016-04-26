#coding:utf-8
import sys
from selenium import webdriver
import time
sys.path.append('./add friends')
ff=webdriver.Firefox()
ff.get("http://54.222.192.204:8081/user/login")
time.sleep(1)
ff.find_element_by_id('login').send_keys('wangchen')
ff.find_element_by_id('password').send_keys('123456')
ff.find_element_by_class_name('save').click()
ff.find_element_by_id("env_total").click()
ff.find_element_by_id('env_total').click()
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='env_total']/option[2]").click()
ff.refresh()
ff.find_element_by_xpath(".//*[@id='status']/ul/li[8]/a").click()
ff.find_element_by_xpath(".//*[@id='list-operationProcedure']/table/tbody/tr/td[1]/a").click()
ff.find_element_by_class_name("edit").click()
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='param']/parent:://").clear()
'''
ff.find_element_by_xpath(".//*[@id='list-body']/tr[1]/td[3]/textarea").clear()
ff.find_element_by_xpath(".//*[@id='list-body']/tr[1]/td[3]/textarea").send_keys('484sa')
ff.find_element_by_xpath(".//*[@id='list-body']/tr[2]/td[3]/textarea").clear()
ff.find_element_by_xpath(".//*[@id='list-body']/tr[2]/td[3]/textarea").send_keys('4842')
'''
# els=ff.find_elements_by_xpath(".//*[@id='param']")
# how_much=len(els)
# print how_much
# for el in els:
#     print el.text
# ".//*[@id='list-body']/tr[1]/td[3]/textarea"
# ".//*[@id='list-body']/tr[2]/td[3]/textarea"
# a={'phone':'1', 'phone':'2', 'phone':'3'}
