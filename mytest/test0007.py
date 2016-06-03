a=['a','a','a','b','b','b','c','c','c','e','e','e']
finall_res=[]

for i in xrange(len(a)):
	res=[]
	if len(a)-i>3 and a[i]==a[i+2]:
		res.append(a[i])
		res.append(a[i+1])
		res.append(a[i+2])
		finall_res.append(res)
	elif len(a)-i==3:
		res.append(a[-3])
		res.append(a[-2])
		res.append(a[-1])
		finall_res.append(res)
	else:
		pass
print res
print finall_res
print len(finall_res)
print finall_res[0][0]
print finall_res[1][0]
print finall_res[2][0]