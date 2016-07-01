#coding:utf-8
import time
import os
from selenium import webdriver
phantomjs_path=os.path.abspath(r"C:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe")
ff=webdriver.PhantomJS(phantomjs_path)
ff.get(r"http://tactics.xingyunzhi.cn/staging/admin.html?uid=577230e0ad037df55ef9fa07&serverId=4001")
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='nick_name']").send_keys(u'佐罗的面具')
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='query_user']/div[4]/input").click()
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='features']/div[1]").click()#.//*[@id='features']/div[1]/h4/a
print ff.find_element_by_xpath(".//*[@id='features']/div[1]/h4/a").text
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='features']/div[2]").click()
print ff.find_element_by_xpath(".//*[@id='features']/div[2]/h4/a").text
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='features']/div[3]").click()
print ff.find_element_by_xpath(".//*[@id='features']/div[3]/h4/a").text
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='features']/div[4]").click()
print ff.find_element_by_xpath(".//*[@id='features']/div[4]/h4/a").text
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='features']/div[5]").click()
print ff.find_element_by_xpath(".//*[@id='features']/div[5]/h4/a").text
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='features']/div[6]").click()
print ff.find_element_by_xpath(".//*[@id='features']/div[6]/h4/a").text
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='features']/div[7]").click()
print ff.find_element_by_xpath(".//*[@id='features']/div[7]/h4/a").text
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='features']/div[8]").click()
print ff.find_element_by_xpath(".//*[@id='features']/div[8]/h4/a").text
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='features']/div[9]").click()
print ff.find_element_by_xpath(".//*[@id='features']/div[9]/h4/a").text
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='features']/div[10]").click()
print ff.find_element_by_xpath(".//*[@id='features']/div[10]/h4/a").text
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='features']/div[11]").click()
print ff.find_element_by_xpath(".//*[@id='features']/div[11]/h4/a").text
time.sleep(1)
ff.find_element_by_xpath(".//*[@id='features']/div[12]").click()
print ff.find_element_by_xpath(".//*[@id='features']/div[12]/h4/a").text
time.sleep(1)

ff.quit()