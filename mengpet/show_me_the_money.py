#coding:utf-8
from selenium import webdriver
import time,os
user_info=open('./input_your_url.txt','r')
a=user_info.readline()
str(a)
user_id=a[50:82]
coin=1000000#金币
cash=100#钻石
social=1000#红心
item1=10000#加速胶囊
item2=10000#减半闪电
admin_url='http://pets.xingyunzhi.cn:3000/admin.html'
#ff=webdriver.Firefox()
phantomjs_path=os.path.abspath(r"C:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe")
ff=webdriver.PhantomJS(phantomjs_path)
ff.get(admin_url)
ff.set_window_size(600,800)
ff.implicitly_wait(10)
ff.find_element_by_id('uid').clear()
ff.find_element_by_id('uid').send_keys(user_id)
ff.find_element_by_id('coin').clear()
ff.find_element_by_id('coin').send_keys(coin)
ff.find_element_by_id('cash').clear()
ff.find_element_by_id('cash').send_keys(cash)
ff.find_element_by_id('social').clear()
ff.find_element_by_id('social').send_keys(social)
ff.find_element_by_id('item1').clear()
ff.find_element_by_id('item1').send_keys(item1)
ff.find_element_by_id('item2').clear()
ff.find_element_by_id('item2').send_keys(item2)
ff.find_element_by_xpath('html/body/p[8]/input[8]').click()
print (u'你已经赢取白富美，正在走向人生巅峰')
print (u'')
time.sleep(2)
ff.quit()