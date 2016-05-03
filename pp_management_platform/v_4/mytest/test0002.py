#coding:utf-8
import sys
from selenium import webdriver
import time
sys.path.append('./mytest')
import test0001
ff=webdriver.Firefox()
ff.get("http://www.baidu.com")
ff.maximize_window()
time.sleep(3)
#大帅的
b=test0001.a
for i in b:
    ff.find_element_by_id('kw').send_keys(i)
    ff.find_element_by_id('su').click()
    if i==2:
        break
    else:
        ff.find_element_by_id('kw').clear()
        time.sleep(5)