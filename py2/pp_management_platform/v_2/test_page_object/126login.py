#coding=utf-8
from selenium import webdriver
import sys
sys.path.append('\package')
from package import location

driver = webdriver.Firefox()
driver.get("http://m.mail.10086.cn")

'''
def id(loc):
	id = driver.find_element_by_id(loc)
	return id
'''
location.id(driver,'ur').clear()
location.id(driver,'ur').send_keys('username')
location.id(driver,'pw').clear()
location.id(driver,'pw').send_keys('password')
location.id(driver,"lnkSubmit").click()

'''
driver.find_element_by_id("ur").clear()
driver.find_element_by_id("ur").send_keys("username")
driver.find_element_by_id("pw").clear()
driver.find_element_by_id("pw").send_keys("password")
driver.find_element_by_id("lnkSubmit").click()
'''
driver.quit()
