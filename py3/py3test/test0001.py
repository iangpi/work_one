'''
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print (A2)
'''
import sys
sys.path.append('D:\mygit\work_one\py3\py3test')
from test0002 import Test
res=Test()
print (res.myadd(1,2))