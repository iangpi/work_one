#coding=utf-8
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from base import Page


class LoginPage(Page):

	'''
	登录页面模型
	'''
	url = '/'
	#定位器
	#find_element_by_id("idInput")
	#find_element(By.ID,'idInput')
	#find_element_by_name("idInput")
	#find_element(By.NAME,'idInput')

	username_loc = (By.ID,"ur")
	password_loc = (By.ID,"pw")
	submit_loc = (By.ID,"lnkSubmit")

	#Action
	def open(self):
		self._open(self.url)
	
	def type_username(self,username):
		self.find_element(*self.username_loc).clear()
		self.find_element(*self.username_loc).send_keys(username)
	
	def type_password(self,password):
		self.find_element(*self.password_loc).clear()
		self.find_element(*self.password_loc).send_keys(password)
	
	def submit(self):
		self.find_element(*self.submit_loc).click()


def test_user_login(driver, username, password):
	"""
	测试获取的用户名密码 是否可以登录
	"""
	login_page = LoginPage(driver)
	login_page.open()
	#login_page.type_username(username)
	login_page.type_password(password)
	login_page.submit()
	sleep(3)
	'''
	un = username+'@126.com'
	'testingwtb@126.com'
	txt = driver.find_element_by_id('xx').text
	'testingwtb@126.com'
	assertEqual(un,txt)
	'''