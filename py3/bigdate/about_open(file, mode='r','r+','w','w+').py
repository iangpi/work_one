'''
详细说明：http://blog.csdn.net/ztf312/article/details/47259805

简单说明：
1:r只读，r+读写，不创建
2:w新建只写，w+新建读写，二者都会将文件内容清零
（以w方式打开，不能读出。w+可读写）
3:w+与r+区别：
r+：可读可写，若文件不存在，报错；w+: 可读可写，若文件不存在，创建


'''
f = open(r'D:\first.txt','w')#尝试写
f.write("1234567890")
#f.read()#w参参数表示新建，但是只能写的，不能读，如果尝试读会报错
f.close()

f=open(r"D:\first.txt",'r')
a0=f.read()#读取整个
print (a0,'读取整个')
f.close()

f=open(r"D:\first.txt",'r')#r表示只可以读但是不能写
a1=f.read(5)#read方法里的参数表示读前5位置，读取游标回到5之后
a2=f.read()#继续读取5以后的部分知道结尾，游标到了结尾l
print (a1,'切片读取',a2,'剩余部分读取')
f.close()

f=open(r"D:\first.txt",'r+')#尝试r+，直接从头部开始覆盖。
f.write('abced')
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
'''
f=open(r"D:\first.txt",'a')
f.write('111')
f.close()

f=open(r"D:\first.txt",'r')
print (f.read())
f.close()
'''
f=open(r"D:\first.txt",'a+')#a+是结尾添加
f.write('222')
f.close()

f=open(r"D:\first.txt",'r')
print (f.read(),'a+是结尾添加')
f.close()