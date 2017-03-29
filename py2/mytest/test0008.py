#coding:utf-8
'''
l1=['a','b','c','d']
l2=['a','d']
res=[]
for i in l1:
    if i in l2:
        res.append(i)
print res
'''
'''
for i in xrange(5):
    print i
print 11111111111111111111
for i in xrange(5,10):
    print i
'''
'''
a=[1,[2,3]]
print len(a)
'''

#coding:utf-8
import os
import json
import time
import sys
import xlwt
reload(sys)
sys.setdefaultencoding('utf8')

path_monster=os.path.abspath(r"D:\mygit\work_one\zhanqi\myjson\monster.json")
path_skill=os.path.abspath(r"D:\mygit\work_one\zhanqi\myjson\skill.json")
path_unlockSkill=os.path.abspath(r"D:\mygit\work_one\zhanqi\myjson\unlockSkill.json")

class hero_card(object):
    def __init__(self):
        #读怪物json
        monster_file=file(path_monster)
        self.read_monster=json.load(monster_file)
        self.monster_num=len(self.read_monster)
        #print ('怪物总数:'),self.monster_num

        #读技能json
        skill_file=file(path_skill)
        self.read_skill=json.load(skill_file)
        self.skill_num=(len(self.read_skill))

        #读天赋json
        unlock_skill_file=file(path_unlockSkill)
        self.read_unlock_skill=json.load(unlock_skill_file)
        self.unlock_skill_num=len(self.read_unlock_skill)

    def all_cards(self):
        #抽取出来玩家的卡牌
        user_cards=[]
        for n in xrange(self.monster_num):
            user_cards.append(self.read_monster[n])
        return user_cards
        #抽取玩家卡牌名字，用作给表格建立分页用
    def all_cards_name(self):
        cards_name=[]
        for n in xrange(self.monster_num):
            cards_name.append(self.read_monster[n]['name'])
        return cards_name
        #抽取玩家卡牌id，
    def all_cards_id(self):
        cards_id=[]
        for n in xrange(self.monster_num):
            cards_id.append(self.read_monster[n]['id'])
        return cards_id

    def all_cards_unlockskill(self):
        unlock_cards_skill=[]#每三个id一样的放到一个小list里，最后放到这个cards_skill里
        for n in xrange(self.unlock_skill_num):
            #在unlock表里，如果一张卡的id和第三张的id相等，那么1，2，3张分别是主动，被动，天赋
            unlock_card_skill=[]
            if self.unlock_skill_num-n>3 and self.read_unlock_skill[n]['id']==self.read_unlock_skill[n+2]['id']:
                unlock_card_skill.append(self.read_unlock_skill[n])
                unlock_card_skill.append(self.read_unlock_skill[n+1])
                unlock_card_skill.append(self.read_unlock_skill[n+2])
                unlock_cards_skill.append(unlock_card_skill)
            elif self.unlock_skill_num-n==3:
                unlock_card_skill.append(self.read_unlock_skill[-3])
                unlock_card_skill.append(self.read_unlock_skill[-2])
                unlock_card_skill.append(self.read_unlock_skill[-1])
                unlock_cards_skill.append(unlock_card_skill)
            else:
                pass
        return unlock_cards_skill
    def get_info(self,skill_id,skill_level):
        for n in xrange(self.skill_num):
            if self.read_skill[n]['id']==skill_id and self.read_skill[n]['level']==int(skill_level):
                res=self.read_skill[n]['desc']
        return res
if __name__=="__main__":
    test=hero_card()
    print test.get_info('skill001','7')