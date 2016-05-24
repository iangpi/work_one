#coding:utf-8
from selenium import webdriver
import time,os
user_info=open('./input_your_url.txt','r')
a=user_info.readline()
str(a)
user_id=a[50:82]
coin=1000000#金币
cash=1000000#钻石
social=1000#红心
item1=10000#加速胶囊
item2=10000#减半闪电
admin_url='http://pets.xingyunzhi.cn:3000/admin.html'
phantomjs_path=os.path.abspath(r"C:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe")
ff=webdriver.PhantomJS(phantomjs_path)
ff.get(admin_url)
ff.set_window_size(600,800)
ff.implicitly_wait(10)
def by_id(the_id,the_value):
    ff.find_element_by_id(the_id).clear()
    ff.find_element_by_id(the_id).send_keys(the_value)
def by_xpaht(the_xpath):
    return
    ff.find_element_by_id()
by_id('uid').clear()
by_id('uid').send_keys(user_id)
by_id('coin').clear()
by_id('coin').send_keys(coin)
by_id('cash').clear()
by_id('cash').send_keys(cash)
by_id()