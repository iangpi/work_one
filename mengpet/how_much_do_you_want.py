#coding:utf-8
from selenium import webdriver
import time,os
user_info=open('./input_your_url.txt','r')
a=user_info.readline()
str(a)
user_id=a[50:82]
#下面的数字，可以填写0，但是不能为空
# coin=0#金币
# cash=100#钻石
# social=0#红心
# item1=0#加速胶囊
# item2=0#减半闪电
admin_url='http://pets.xingyunzhi.cn:3000/admin.html'
phantomjs_path=os.path.abspath(r"C:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe")
ff=webdriver.PhantomJS(phantomjs_path)
ff.get(admin_url)
ff.implicitly_wait(10)
ff.find_element_by_id('uid').clear()
ff.find_element_by_id('uid').send_keys(user_id)
ff.find_element_by_id('coin').clear()
while True:
    coin=raw_input('你要多少金币？'.decode('utf-8').encode('gbk'))
    if coin.isdigit():#isdigit,数字返回True，菲数字返回false
        break
ff.find_element_by_id('coin').send_keys(coin)
ff.find_element_by_id('cash').clear()
while 1:
    cash=raw_input("你要多少钻？".decode('utf-8').encode('gbk'))
    if cash.isdigit():
        break
ff.find_element_by_id('cash').send_keys(cash)
ff.find_element_by_id('social').clear()
while True:
    social=raw_input("你要多少红心？".decode('utf-8').encode('gbk'))
    if social.isdigit():
        break
ff.find_element_by_id('social').send_keys(social)
ff.find_element_by_id('item1').clear()
while True:
    item1=raw_input("你要多少秒表？".decode('utf-8').encode('gbk'))
    if item1.isdigit():
        break
ff.find_element_by_id('item1').send_keys(item1)
ff.find_element_by_id('item2').clear()
while True:
    item2=raw_input("你要多少胶囊？".decode('utf-8').encode('gbk'))
    if item2.isdigit():
        break
ff.find_element_by_id('item2').send_keys(item2)
ff.find_element_by_xpath('html/body/p[8]/input[8]').click()
print (u'你已经赢取白富美，正在走向人生巅峰')
time.sleep(2)
ff.quit()

