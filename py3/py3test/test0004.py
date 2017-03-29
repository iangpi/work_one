__author__ = 'ppldc'
#关于判断数据类型的方法
a=1
print (a,'is int',isinstance(a,int))

b='abc'
print (b, 'is str',isinstance(b,str))

c=[1,2]
print (c, 'is list',isinstance(c,list))

d=('w','x')
print (d, 'is tuple',isinstance(d,tuple))

e={'a':1}
print (e,'is dict',isinstance(e,dict))


l=[1,'a']
for i in l:
    if isinstance(i,int):
        print (i)
    elif isinstance(i,str):
        print (i)
