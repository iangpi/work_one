#coding:utf-8
'''以qq首页，登录qq为例子，弹出的登录框，就是在iframe中'''
from selenium import webdriver
from time import sleep

dr=webdriver.Firefox()
dr.get("http://www.qq.com")
dr.find_element_by_id('loginGrayLayout').click()
sleep(5)
frame=dr.find_element_by_id('login_frame')
dr.switch_to.frame(frame)

sleep(3)
dr.find_element_by_name('u').send_keys('username')

sleep(3)
dr.quit()