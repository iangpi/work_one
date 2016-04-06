#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Page(object):
	'''
	基本类，用于所页面的继承
	'''
	mail_url = 'http://m.mail.10086.cn'
	def __init__(self, selenium_driver, base_url=mail_url, parent=None):
		self.base_url = base_url
		self.driver = selenium_driver
		self.timeout = 30
		self.parent = parent
		self.tabs = {}

	def _open(self,url):
		url = self.base_url + url
		self.driver.get(url)
		assert self.on_page(), 'Did not land on %s' % url
	
	def find_element(self,*loc):
		return self.driver.find_element(*loc)
	
	def open(self):
		self._open(self.url)
	
	def on_page(self):
		return self.driver.current_url == (self.base_url + self.url)
	
	def script(self,src):
		return self.driver.execute_script(src)
	
	def send_keys(self,loc,value, clear_first=True, click_first=True):
		try:
			loc = getattr(self, '_%s' % loc) 
			if click_first:
				self.find_element(*loc).click()
			if clear_first:
				self.find_element(*loc).clear()
			self.find_element(*loc).send_keys(value)
		except AttributeError:
			print '%s page does not have "%s" locator' %(self,loc)

#page object
class LoginPage(Page):

	'''
	登录页面模型
	'''
	url = '/'
	username_loc = (By.ID,"ur")
	password_loc = (By.ID,"pw")
	submit_loc = (By.ID,"lnkSubmit")
	
	#Action
	def open(self):
		self._open(self.url)
	
	def type_username(self,username):
		self.find_element(*self.username_loc).send_keys(username)
	
	def type_password(self,password):
		self.find_element(*self.password_loc).send_keys(password)
	
	def submit(self):
		self.find_element(*self.submit_loc).click()


def test_user_login(driver, username, password):
	"""
	测试获取的用户名密码 是否可以登录
	"""
	login_page = LoginPage(driver)
	login_page.open()
	login_page.type_username(username)
	login_page.type_password(password)
	login_page.submit()
	sleep(3)
	#assert(username == 'testingwtb@126.com'),u"用户名称不匹配，登录失败!"

def main():
	try:
		# Selenium
		driver = webdriver.Firefox()
		username = 'username'
		password = 'password'
		test_user_login(driver,username,password)	
	finally:
		# 关闭浏览器窗口
		driver.quit()

if __name__ == '__main__':
	main()