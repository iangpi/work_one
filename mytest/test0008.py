l1=['a','b','c','d']
l2=['a','d']
res=[]
for i in l1:
    if i in l2:
        res.append(i)
print res
