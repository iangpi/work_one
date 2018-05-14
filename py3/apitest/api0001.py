'''
lists=[]
for i in range(23):
	lists.append([])
print (lists)
print (len(lists))
lists=[ [ ] for i in range(5) ]
print (len(lists))
print (160/60.0)
'''
f = open(r'D:\first.txt','w')#尝试写
f.write("1234567890")
#f.read()#w参参数表示新建，但是只能写的，不能读，如果尝试读会报错
f.close()

f=open(r"D:\first.txt",'r')#r表示只可以读但是不能写
a1=f.read(5)#read方法里的参数表示读前5位置，读取游标回到5之后
a2=f.read()#继续读取5以后的部分知道结尾，游标到了结尾l
print (a1,a2)
f.close()

f=open(r"D:\first.txt",'r+')#尝试r+
f.write('abc')
print (f.read(),'被r+方法改写到了第3位，只读到游标3以后的')
f.close()

f=open(r"D:\first.txt",'r')#读取r+之后的
a3=f.read()
print (a3,'读到了被改写以后的文件')
f.close()

f=open(r"D:\first.txt",'w+')#直接清空当前文件，重新写。
f.write('xyz')
f.close()

f=open(r"D:\first.txt",'r')
print (f.read(),'以当读取的时候发现，只有xyz，之前的都被w+操作覆盖了，w+就是清空+重新写入新的）')
f.close()