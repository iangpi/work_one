#coding:utf-8
import time
import requests
'''
r=requests.get('http://www.baidu.com')
print r.status_code


d=r.request.headers
print 'd:',d
for k,v in d.items():
    print "%s:%s" %(k,v)



print r.headers
print r.headers.get('X-UA-Compatible')
print r.headers.get('BDQID')


#支持josn传输格式,也支持protobuffer传输格式

r=requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=122.88.60.28')
print r.json()['data']['country']



requests.get('http://github.com', timeout=10.001)
'''

'''
print 'start time is:',time.strftime("%Y-%m-%d %H_%M_%S")
try:
    requests.get('http://github.com', timeout=10.001)
    print 'end time is:',time.strftime("%Y-%m-%d %H_%M_%S")
except:
    print 'if time out,print end time is:',time.strftime("%Y-%m-%d %H_%M_%S")
else:
    pass
'''

list = ['a','b','c']
str = ('').join(list)
print str[0],type(str[0])