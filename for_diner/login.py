#coding:utf-8
from selenium import webdriver

filename=r"your_info.txt"
mylist=[]
lines=open(filename,'r').readlines()
for line in lines:
    line=line.strip('\n')
    mylist.append(line)
email=(mylist[0])
password=(mylist[1])

ff=webdriver.Firefox()
ff.implicitly_wait(30)
ff.get(r"http://meican.com/login")
ff.find_element_by_id("email").clear()
ff.find_element_by_id("email").send_keys(email)
ff.find_element_by_id("password").clear()
ff.find_element_by_id("password").send_keys(password)
ff.find_element_by_id("signin").click()