import os
path=os.path.abspath(r"D:\mygit\work_one\py3\bigdate\avatar.txt")
f=open(path)
lines=f.readlines()
num=0
res=[]#数据存成列表
for line in lines:	
	res.append(line)
	num=num+1
ends=[]#准备存放所有图片结尾格式
begins=[]
for i in range(len(res)):#遍历整理后的列表长度
	ends.append(res[i][-4:-1])#只取每个list的后三位，就能区分到底是什么格式的图的后缀名了

	begins.append(res[i][0:26])
finall_end=list(set(ends))#接收去重后的图片格式

finall_begin=list(set(begins))#接收去重后的网址
print ('图片格式一共：',len(finall_end),'个')
print (finall_end)
#print ('网址类型一共：',len(finall_begin),'个',finall_begin)
res.sort()

https=[]
nums=[]
for n in range(len(res)):
	#print (res[n])
	if n<=len(res)-3 and res[n][0:22]==res[n-1][0:22] and res[n][0:22]==res[n-2][0:22] and res[n][0:22]!=res[n+1][0:22]:
		print (n,res[n])
		nums.append(n)
		https.append(res[n])
	elif n<=len(res)-3 and res[n][0:22]==res[n-1][0:22] and res[n][0:22]!=res[n-2][0:22] and res[n][0:22]!=res[n+1][0:22]:
		print (n,res[n],'只有2个')
		nums.append(n)
		https.append(res[n])
	elif n<=len(res)-3 and res[n][0:22]!=res[n-1][0:22] and res[n][0:22]!=res[n+1][0:22]:
		print (n,res[n])
		nums.append(n)
		https.append(res[n])
	else:
		pass

'''
['\n', 
'/0\n', 
'figureurl_qq_2\n', 
'http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png\n', 
'http://g.cdn.pengpengla.com/oauthgame/moren.png\n', 
'http://p.cdn.pengpengla.com/uplive/p/u/2016/9/9/fc069f9b-2b56-4238-ad04-a79efadb41ab.jpg\n', 
'http://p.cdn.pepper.world/uplive/p/u/2016/9/9/fbb546c9-9f4e-4f65-afe8-ca34b15ebd2d.jpg\n', 
'http://p.cdn.upliveapps.com/uplive/p/u/2017/8/1/ffa2b8f0-5678-45ff-9ff3-bce567fb903c.jpg\n', 
'http://p.pengpengla.com/guestavatar/m_1087.jpg\n',
'http://p.upcdn.pengpengla.com/uplive/p/u/2017/8/1/a3657614-3ace-4837-9f76-22e9eab2e410.jpg\n',
'http://p.wscdn.upliveapp.com/uplive/p/u/2017/7/17/18575816_1500279068601.jpg\n', 
'http://pbs.twimg.com/profile_images/833900990285746176/LQeea7Wq_normal.jpg\n', 
'http://q.qlogo.cn/qqapp/1106102904/C1996814805B49A74D0BE141A234A3AD/100\n',
'http://wx.qlogo.cn/mmhead/wprMnqDUJH67ROczm79TLmQ8gF3lTliaXHswJXx8erQEaH1K1KLGdaQ/0\n',
'http://wx.qlogo.cn/mmopen/lEgP1Qs2iaUN2fVTxqbZeMzyibMibBCNRQk4Cc0Yv7dY3w3BfPItuprxiaR3HNs4FVib8Wic9G9EGL3sgxxRhQ0hiaFJWPia8SAwLNtE/0\n', 
'https://graph.facebook.com/me/picture?access_token=EAAYInDT7wLQBAP5syzvNgawrwUA6a7MAZAqqs0c4MlWStvQRJDSNqZABnECCH0QnvYISDfHDpnrwti2parcx7vbSkp43nR4aBRk9JoBJurZAafjaIfyJ86ZCJLJAi9ZColPISlcaKSSmZCnFp5mxsWGKxLPpLvnoLWCXzEZCAuzZBtp1n3yDvP3m\n', 
'https://lh3.googleusercontent.com/-rGXpi-ejGg0/AAAAAAAAAAI/AAAAAAAAAAA/AI6yGXz8ACzillzsNgwwvRnTFRDZMoBxtQ/s96-c/photo.jpg\n', 
'https://lh4.googleusercontent.com/-ys1e-do23Fw/AAAAAAAAAAI/AAAAAAAAAAA/AI6yGXyz2_8J3e4C-fbu-wu1t_KeGDPYcg/s96-c/photo.jpg\n', 
'https://lh5.googleusercontent.com/-xT9yNxamTwM/AAAAAAAAAAI/AAAAAAAAAAA/AAyYBF7cRjVGBSkCte2PUa_SVIXAeYTZPA/s96-c/photo.jpg\n', 
'https://lh6.googleusercontent.com/-yVtaN0o6Iqs/AAAAAAAAAAI/AAAAAAAAAAw/MGQS20_sAq4/s96-c/photo.jpg\n', 
'https://pbs.twimg.com/profile_images/832498411127443456/d_ZC3T_Y_reasonably_small.jpg\n']
'''