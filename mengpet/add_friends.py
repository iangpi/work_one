#coding:utf-8
from selenium import webdriver
from time import sleep
user_info=open('./input_your_url.txt','r')
a=user_info.readline()
str(a)
user_id=a[50:82]
admin_url='http://pets.xingyunzhi.cn:3000/admin.html'
ff=webdriver.Firefox()
ff.get(admin_url)
ff.implicitly_wait(10)
ff.find_element_by_id('add_Friend').send_keys(user_id)#默认直接加了20个好友
ff.find_element_by_xpath('html/body/p[6]/input[2]').click()
print (u'你已经添加了20个好友')
sleep(2)
ff.quit()