#coding:utf-8
import json
# import sys
# sys.path.append('./zhanqi')
f = file("skill.json");
s = json.load(f)

search={'弓箭手':{'skill_id':'skill061'}}


num=(len(s))
skills=[]
for n in xrange(num):
    if s[n]['id']==search['弓箭手']['skill_id']:
        print '在list中第',n,'个//','技能名字是：',s[n]['name'],'//技能描述是：',s[n]['desc']
        pass
f.close()

