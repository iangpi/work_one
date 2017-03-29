#coding:utf-8
'''
__author__ = 'Chris'
#coding:utf-8
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
sys.path.append('./add friends')
ff=webdriver.Firefox()
ff.get("http://54.222.192.204:8081/user/login")
time.sleep(2)
ff.find_element_by_id('login').send_keys('wangchen')
ff.find_element_by_id('password').send_keys('123456')
ff.find_element_by_class_name('save').click()
#点击Link1链接（弹出下拉列表）
ff.find_element_by_id("env_total").click()
time.sleep(2)
#找到id 为dropdown1的父元素
WebDriverWait(ff, 10).until(lambda the_driver: the_driver.find_element_by_id('dropdown1').is_displayed())
#在父亲元件下找到link为Action的子元素
menu=ff.find_element_by_id('dropdown1').find_element_by_link_text('Action')

#鼠标定位到子元素上
webdriver.ActionChains(ff).move_to_element(menu).perform()

#webdriver.ActionChains(ff).move_to_element(".//*[@id='env_total']/option[2]").perform()
#ff.find_element_by_xpath(".//*[@id='env_total']/option[2]").click()
time.sleep(2)
#ff.find_element_by_xpath(".//*[@id='env_total']/option[2]").click()
#ff.find_element_by_xpath(".//*[@id='env_total']/option[1]").click()
'''

'''
a=parameter.b
for i in a:
    ff.find_element_by_id('kw').send_keys(i)
    ff.find_element_by_id('su').click()
    ff.find_element_by_id('kw').clear()
time.sleep(5)
ff.quit()
'''

'''这个例子告诉我们，定位方法，是不能传字典的
import time
from selenium import webdriver
ff= webdriver.Firefox()
ff.get('http:www.baidu.com')
ff.find_element_by_id('kw').send_keys('python')
ff.find_element_by_id('su').click()
ff.maximize_window()
time.sleep(3)
ff.find_element_by_xpath(".//*[@id='2']/div[1]/div[1]/a/img").click()
'''

#复习，xpath利用层级和属性and组合定位的方法
from selenium import webdriver
ff=webdriver.Firefox()
ff.get(r"http://www.baidu.com")
ff.find_element_by_xpath("//span/input[@id='kw' and @class='s_ipt']").send_keys('123')
