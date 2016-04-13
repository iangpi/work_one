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
mylist=[line.split('\n') for line in lines]
a,b=mylist[0],mylist[1]
email,password=','.join(a),','.join(b)
print email,type(email)
print password,type(password)
'''

'''
filename=r"your_info.txt"
mylist=[]
lines=open(filename,'r').readlines()
for line in lines:
    line.strip('\n')
    mylist.append(line)
email=(mylist[0])
password=(mylist[1])
print email,password
'''

'''list转换为str
l=['a','b']
a=','.join(l)
print(a)
'''
'''切片功能，切除前后特定字符，默认为空，可以字符串形式入参，
str = "0000000this is string example....wow!!!0000000";
print str.strip( '0' );
print str
'''