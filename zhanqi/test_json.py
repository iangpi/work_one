#coding:utf-8
import time
import json
import os
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

'''
print time.ctime()
def a():
    for n in xrange(10):
        if n==9:
            a=n
    return a
if __name__=="__main__":
    a()
    print time.ctime()
'''
'''
还能这样断言的

a='123'
b='1'
c='6'
assert (b in a) and (c in a)
assert (b in a) or (c in a)
'''

'''
#读取json后，不能显示中文的解决方案，但是结果是unicode
path_monster=os.path.abspath(r"D:\mygit\work_one\zhanqi\myjson\monster.json")
monster_file=file(path_monster)
read_monster=json.load(monster_file)
print read_monster[0]
print type(read_monster[0])


path_monster=os.path.abspath(r"D:\mygit\work_one\zhanqi\myjson\monster.json")
monster_file=file(path_monster)
read_monster=json.loads(monster_file.read())
read_monster_again=json.dumps(read_monster,ensure_ascii=False)

print read_monster_again[0]
print type(read_monster_again[0])

'''

'''
def w():
    l=[1,2,3]
    for n in xrange(len(l)):
        res=l[n]
    return res
print w()
'''
'''
#coding:utf-8
import os
import json
import time
import sys
import xlwt
reload(sys)
sys.setdefaultencoding('utf8')

path_monster=os.path.abspath(r"D:\mygit\work_one\zhanqi\myjson\monster.json")
monster_file=file(path_monster)
read_monster=json.load(monster_file)
print read_monster[0]
'''


a=[2,8,3]
a.sort()
print a
