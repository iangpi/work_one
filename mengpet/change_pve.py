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
ff.set_window_size(60,80)
ff.implicitly_wait(5)
ff.find_element_by_id('pve_uid').send_keys(user_id)
# pve_level=raw_input("小婊砸，想跳到哪一关？".decode('utf-8').encode('gbk'))
while 1:
    pve_level=raw_input("输入一个你想到达的关卡？".decode('utf-8').encode('gbk'))
    if pve_level.isdigit():
        break
ff.find_element_by_id('pve_level').send_keys(pve_level)
ff.find_element_by_xpath('html/body/p[10]/input[3]').click()
ff.implicitly_wait(5)
print ('已经调整好等级了'.decode('utf-8').encode('gbk'))
ff.quit()