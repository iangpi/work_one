#coding:utf-8
from selenium import webdriver
import os
import time
print time.ctime()

#用户名字和想要卡牌数量参数化
test_address=r"http://tactics.xingyunzhi.cn/delta/admin.html"

#nick_name='Houlin'
#nick_name=u'奇怪的选手'
#nick_name=u'不大不小超'
nick_name=u'葫芦娃二娃'
#nick_name='shunia'#包子

#dr=webdriver.Firefox()
#无界面浏览器
phantomjs_path=os.path.abspath(r"C:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe")
dr=webdriver.PhantomJS(phantomjs_path)
dr.get(test_address)
time.sleep(1)

#查找用户
dr.find_element_by_id('server_id').clear()
dr.find_element_by_id('server_id').send_keys('7001')
dr.find_element_by_id('nick_name').send_keys(nick_name)
dr.find_element_by_xpath(".//*[@id='query_user']/p[5]/input").click()
time.sleep(1)
dr.find_element_by_id('cb_remove_user').click()
dr.find_element_by_xpath(".//*[@id='features']/p[2]/input[2]").click()
dr.quit()
print time.ctime()