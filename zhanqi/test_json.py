#coding:utf-8
'''
import json
s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
print s
print s.keys()
print s["name"]
print s["type"]["name"]
print s["type"]["parameter"][1]
'''

'''
a=int(9)
print '%d'%a
'''

'''

for a in xrange(0,10,3):
    b=a+1
    print b
for a in xrange(11,20,2):
    b=a+1
    print b
'''

def a():
    for n in xrange(10):
        if n==9:
            a=n
    return a
if __name__=="__main__":
    a()