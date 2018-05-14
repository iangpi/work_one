print (63832+750)
print ((20+50+80+120+160+200)*2-20+822)
'''
1，进入各种老虎机，显示账号是吃肉的小花
2，点击hud的齿轮，就回到了大厅
3，水果机进不去
4，没有任务


'''
for i in range(1,10,2):
	print (i)
	if i%5==4:
		print ('bbbb')
		break
else:
	print (i)

def myaddstr(x):
	'str+str'
	return(x+x)
print (myaddstr.__doc__)#用来查看函数说明文字的
print (myaddstr(1))