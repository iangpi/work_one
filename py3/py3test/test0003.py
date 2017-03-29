#无限迭代器
#迭代数字
import itertools
nums=itertools.count(6)
for i in nums:
	if i > 10:
		break
	print (i)
#迭代字符串
strs=itertools.cycle('lidachao1')
for i in strs:
	if i =='1':
		break
	print (i)
#第二个参数可以限制条件,重复次数
strs1=itertools.repeat('a',5)
for i in strs1:
	print (i)