#coding:utf-8
from selenium import webdriver
import time,os
user_info=open('./input_your_url.txt','r')
a=user_info.readline()
str(a)
user_id=a[50:82]
admin_url='http://pets.xingyunzhi.cn:3000/admin.html'
#ff=webdriver.Firefox()
phantomjs_path=os.path.abspath(r"C:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe")
ff=webdriver.PhantomJS(phantomjs_path)
ff.get(admin_url)
ff.set_window_size(600,100)
ff.implicitly_wait(5)
ff.find_element_by_id('level_uid').send_keys(user_id)
#判断是否输入数字
while 1:
    your_level=raw_input("小婊咋，快说你要多少级：".decode('utf-8').encode('gbk'))
    if your_level.isdigit():#
        break
ff.find_element_by_id('level_level').send_keys(your_level)
ff.find_element_by_xpath('html/body/p[12]/input[3]').click()
time.sleep(2)
ff.quit()