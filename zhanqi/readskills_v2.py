#coding:utf-8
import json
import time
'''

#读取怪物表
monsters_file=file("monster.json")
search_monsters=json.load(monsters_file)
monsters_num=len(search_monsters)

#获取天赋表，包括主动技能，被动技能，天赋
skill_file=file("skill.json")
search_skill=json.load(skill_file)
skill_num=len(search_skill)

#获取天赋表
unlock_skill_file=file("unlockSkill.json")
search_unlock_skill=json.load(unlock_skill_file)
unlock_skill_num=len(search_unlock_skill)
'''

'''
需要写几个函数，专门返回怪物id和对应主要技能id的
'''

class hero_card(object):
    def __init__(self,the_id):
        self.the_id=the_id
        #怪物表获取
        self.monster_file=file("monster.json")
        self.read_monster=json.load(self.monster_file)
        self.monster_num=len(self.read_monster)
        print ('当前怪物表怪物总数为:'),self.monster_num

        #技能表获取
        self.skill_file=file("skill.json")
        self.read_skill=json.load(self.skill_file)
        self.skill_num=(len(self.read_skill))

        #获取天赋表
        self.unlock_skill_file=file("unlockSkill.json")
        self.read_unlock_skill=json.load(self.unlock_skill_file)
        self.unlock_skill_num=len(self.read_unlock_skill)

    def get_monsters_by_id(self):
        for n in xrange(self.monster_num):
            if self.read_monster[n]['id']=='monster'+self.the_id:
                a='单位id是：'+str(self.read_monster[n]['id'])
        return a
                # print '代为名称是：',self.read_monster[n]['name']
                # print '输出类型（1是物理，2是法术）：',self.read_monster[n]['type']
                # print '单位类型：',self.read_monster[n]['subType']
                # print '卡牌类型（1是防御，2是输出，3是辅助）：',self.read_monster[n]['unitType']
                # print '解锁级别',self.read_monster[n]['unlockLevel']
                # print '是否可手机（1是可收集，2是不可）：',self.read_monster[n]['collectable']
                # print '是否可移动：',self.read_monster[n]['moveable']
                # print '单位描述：',self.read_monster[n]['desc']

    def skills(self):
        pass

    def unlock_skill(self):
        for n in xrange(self.unlock_skill_num):
            if self.read_unlock_skill[n]['id']=='monster'+self.the_id:
                #主动技能是1，前10级技能是+3步进，后10级技能是+2步进
                if self.read_unlock_skill[n]['type']==1:
                    print ('主动技能如下：')
                    for x in xrange(0,10,3):
                        print self.read_unlock_skill[n]['skillLevel'+str(x+1)],'级技能的','解锁等级是：',x+1
                    for y in xrange(11,20,2):
                        print self.read_unlock_skill[n]['skillLevel'+str(y+1)],'级技能的','解锁等级是：',y+1
                #被动技能是2
                elif self.read_unlock_skill[n]['type']==2:
                    print ('被动技能如下')
                    for x1 in xrange(0,10,3):
                        if self.read_unlock_skill[n]['skillLevel'+str(x1+1)]==None:
                            pass#没有技能可以学习就不打印
                        else:
                            print self.read_unlock_skill[n]['skillLevel'+str(x1+1)],'级技能的','解锁等级是：',x1+1
                    for y1 in xrange(11,20,2):
                        if self.read_unlock_skill[n]['skillLevel'+str(y1+1)]==None:
                            pass
                        else:
                            print self.read_unlock_skill[n]['skillLevel'+str(y1+1)],'级技能的','解锁等级是：',y1+1

                #天赋技能是3
                else:
                    print ('天赋技能如下')
                    for x2 in xrange(0,10,3):
                        if self.read_unlock_skill[n]['skillLevel'+str(x2+1)]==None:
                            pass
                        else:
                            print self.read_unlock_skill[n]['skillLevel'+str(x2+1)],'级技能的','解锁等级是：',x2+1
                    for y2 in xrange(11,20,2):
                        if self.read_unlock_skill[n]['skillLevel'+str(y2+1)]==None:
                            pass
                        else:
                            print self.read_unlock_skill[n]['skillLevel'+str(y2+1)],'级技能的','解锁等级是：',y2+1



if __name__=="__main__":
    test01=hero_card('003')
    print ('-----------------------卡牌基础属性-----------------------')
    print test01.monsters()
    time.sleep(1)
    print ('-----------------主动技能，被动技能，天赋--------------------')
    test01.unlock_skill()
