#coding:utf-8
'''
import sys
from selenium import webdriver
sys.path.append('./mytest')
import test0001
print test0001.a
'''
# import time
# test_time=time.strftime("%Y_%m_%d_%H_%M_%S")
# print test_time
# print type(test_time)

# import requests
# r=requests.get("http://www.baidu.com")
# print r.status_code

#引用一个文件里不通的类的方法
# from test0001 import a
# from test0001 import b
# a=a()
# print a.aa(1,2)
# b=b()
# print b.aaa(3)
'''对list和dict潜逃格式的读取
a=[
 {"name": "ONE","cities": {"city": ["1", "2"]}},
 ]
print a[0]
print a[0]['cities']
print a[0]['cities']['city']
print a[0]['cities']['city'][0]
'''