#coding:utf-8
import time
import sys
from selenium import webdriver
sys.path.append('./mybase')
import mybase
#获取用户信息，返回list
mylist=[]
lines=open("your_info.txt",'r').readlines()
for line in lines:
    line.strip('\n')
    mylist.append(line)
email=mylist[0]
password=mylist[1]

#开始启动浏览器
ff=webdriver.Firefox()
ff.get(mybase.diner_url)
ff.find_element_by_id('password').send_keys(password)
ff.find_element_by_id('email').send_keys(email)
#妈达这个千古奇葩的网站，用户名和密码输入正确后，就自动登陆，不用点击登录按钮，气死宝宝了！
#ff.find_element_by_id('signin').click()
#调用js脚本
js=mybase.js
ff.execute_script(js)

ff.implicitly_wait(10)
ff.find_element_by_xpath(mybase.el_today_diner).click()
ff.implicitly_wait(10)
#所有饭店列表
shops=ff.find_elements_by_class_name("rest-inner")
print '本周有',len(shops)-1,'家家饭店：'
n=-1
for shop in shops:
    n=n+1
    shops_name=(shop).text
    print n,shops_name
time.sleep(3)
ff.quit()