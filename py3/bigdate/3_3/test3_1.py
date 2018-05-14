list_week=['maonday', 'tuesday','wendesday', 'thursday', 'friday', 'saturday','sunday']
print (list_week[0:5])#对lsit进行切片，不包含最后一位，实际是切出来了0，1，2，3，4这5个位置的元素
print (list_week[-7:-2])
print (list_week[::-1])#逆序
print (list_week[::-2])#逆序，间隔2输出
#序列类型转换工厂函数
a=('lidachao')
print (list(a))
print (tuple(a))
b=['lidachao']
print (b,type(b))
print (str(b),type(str(b)))
#其他内置函数。有一些我也没用过,enumerate(sequence, [start=0]),enumerate是枚举的意思
seasons=['spring','simmer','fall','winter']
print (list(enumerate(seasons)))
print (list(enumerate(seasons,start=1)))
#深入展开
print (tuple(enumerate(seasons)))
print (dict(enumerate(seasons)))
#继续深入展开,普通的for循环
i=0
list1=['one','two','three']
for el in list1:
	print (i,list1[i])
	i=i+1

#继续继续深入展开，使用enumerate的循环
list2=['one','two','three']
print (list(enumerate(list2)))#看看enumerate(list2)里面到底是什么
for x,el in enumerate(list2):#for x,el in [(0,'one'),(1,'two'),(2,'three')]:相当于这句，
	print (x,list2[x])

#reversed,返回一个逆向排序的迭代器
list3=[1,2,3,4]
for i in reversed(list3):
	print (i,type(i))
#max and min函数，取最大
print (max(1,3234,-54))
print (min(1,3234,-54))
#sum 函数，相加
print (sum([1,2,3,4],-10))#先在list里加法，然后出来再和负10做加法

w1=[1,2,3]
w2=[4,5,6]
w3=['one','two ','three','four']
w4=[]

print (zip(w1,w2))
for w in zip(w1,w2):
	w4.append(w)
print (w4)


for w in zip(w1,w3):
	w4.append(w)
print (w4)#zip两个list的时候，两个list长短不同，以短的为准


w5=[]
for w in zip(*zip(w1,w2)):#星号啥意思呢？没懂啊。我想想,书上说是解压的意思
	w5.append(w)
print (w5)
#哦，懂了，原来w1和w2是2个单独的list，zip是把他们各自抽出一个元素揉在一起了。
#现在*zip是解压缩，又他们拆散还原回去2个tuple了
'''
总结
zip是压缩，通俗讲是组队
*zip是反压缩，通俗讲就是拆队、
有些函数真的是可以提高生活质量啊
------------------
1.在底部菜单栏增加游戏入口，点击直接进入游戏大厅——pass
2.在直播间增加游戏入口（直播间飘窗位），点击进入直播loading页面，再进入游戏大厅——pass
3.大陆、台湾、香港、新马澳地区上繁体中文；国际区和越南上英文；——pass
4.游戏和直播不并存，切换到游戏大厅时切断直播——pass
------------------------
H5和游戏大厅涉及到的协议有3个。

1、点击充值。去H5的充值页面。——pass
2、点击登录。直接走H5的登录
3、游戏中U钻的消耗以及变化。H5页面会同步U钻数量-pass

-------
1、u币不足，点击确定，没跳转到充值界面
2、大厅中，赛龙舟的icon没有
'''