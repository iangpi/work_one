#coding:utf-8
import time
from selenium import webdriver
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
ff.get(r"http://meican.com/login")
ff.find_element_by_id('password').send_keys(password)
ff.find_element_by_id('email').send_keys(email)
#妈达这个千古奇葩的网站，用户名和密码输入正确后，就自动登陆，不用点击登录按钮，气死宝宝了！
#ff.find_element_by_id('signin').click()
'''
time.sleep(3)
menus1=ff.find_elements_by_class_name("rest-inner")
for menu1 in menus1:
    if menu1.text==u'禾道快餐':
        menu1.click()
js='var hm = document.createElement("script");var s = document.getElementsByTagName("script")[0];s.parentNode.insertBefore(hm, s);'
ff.execute_script(js)
time.sleep(3)
ff.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[2]/ul/li[6]").click()
'''
time.sleep(2)
ff.find_element_by_xpath("html/body/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li/a").click()
time.sleep(2)
ff.find_element_by_xpath("html/body/div[1]/div[2]/div/div[2]/ul/li[3]/a/div").click()
js='var hm = document.createElement("script");var s = document.getElementsByTagName("script")[0];s.parentNode.insertBefore(hm, s);'
ff.execute_script(js)
time.sleep(2)
ff.find_element_by_xpath("html/body/div[1]/div[3]/div/div[2]/div/div[3]/div/a").click()
time.sleep(2)
ff.find_element_by_xpath("html/body/div[1]/div[3]/div/div[2]/div/div[3]/div/a").click()
time.sleep(2)
print ff.find_element_by_xpath("html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[3]/ul/li[1]/div[2]/div[3]/div[1]/div[1]").text


time.sleep(3)
ff.quit()
