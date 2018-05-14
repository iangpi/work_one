'''关于打印和换行'''
'''
print ('1''\n''2''\n''3')
list1=[1,2,3,4]
print (list1[::2])
'''

def fangjia(a,b,c=12):#a是起始金额，b是跌幅百分比，c是跌幅多少个月
	for i in range(c):
		if i<c-1:
			a=a-(a*b)
		else:
			return a
print (fangjia(6.5,0.01))