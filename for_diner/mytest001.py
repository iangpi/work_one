#coding:utf-8
'''列表解析式的例子
mylist=[1,2]
a=[i+1 for i in mylist]
print a
'''
'''遍历后都放入列表里
a = []
for x in [1,2,3,4,5,6,7,8,9,10,11]:
    a.append(x)
print a
'''

'''
filename=r"your_info.txt"
mylist=[]
lines=open(filename,'r').readlines()
mylist=[line.strip().split(',') for line in lines]
print mylist
a,b=mylist[0],mylist[1]
email,password=','.join(a),','.join(b)
print email
print password
'''

'''
filename=r"your_info.txt"
mylist=[]
lines=open(filename,'r').readlines()
for line in lines:
    line=line.strip('\n')
    mylist.append(line)
email=(mylist[0])
password=(mylist[1])
'''


'''list转换为str
l=['a','b']
a=','.join(l)
print(a)
'''
import time
from selenium import webdriver
ff=webdriver.Firefox()
time.sleep(2)
ff.refresh()
time.sleep(2)
ff.refresh()
ff.get(r"http://www.baidu.com")