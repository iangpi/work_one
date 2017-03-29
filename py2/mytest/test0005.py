'''
def Twenty(n=1):
    while n<=20:
        print n
        n=n+1
Twenty()
'''
'''
for i in xrange(20):
    print i

'''
'''
while 1==1:
    print 1
else:
    print 2
'''
res1=[]
res2=[]
for i in xrange(5):
    res1.append(i)
for a in xrange(5):
    res2.append(a)
for n in xrange(len(res1)):
    print [res1[n],res1[n]]
    print type([res1[n],res1[n]])
