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
path_unlockSkill=os.path.abspath(r"D:\mygit\work_one\zhanqi\myjson\monster.json")

class hero_card(object):
    def __init__(self):
        #怪物表获取
        self.monster_file=file(path_monster)
        self.read_monster=json.load(self.monster_file)
        self.monster_num=len(self.read_monster)
        print ('当前怪物表怪物总数为:'),self.monster_num

        #技能表获取
        self.skill_file=file(path_skill)
        self.read_skill=json.load(self.skill_file)
        self.skill_num=(len(self.read_skill))

        #获取天赋表
        self.unlock_skill_file=file(path_unlockSkill)
        self.read_unlock_skill=json.load(self.unlock_skill_file)
        self.unlock_skill_num=len(self.read_unlock_skill)

        self.user_cards=[]
        for n in xrange(self.monster_num):
            if self.read_monster[n]['collectable']==1:
                self.user_cards.append(self.read_monster[n]['id'])
        self.res1=sorted(self.user_cards)

        self.monster_cards=[]
        for n in xrange(self.monster_num):
            if self.read_monster[n]['collectable']==0:
                self.monster_cards.append(self.read_monster[n]['id'])
        self.res2=sorted(self.monster_cards)


    def get_card_info(self):
        for n in xrange(self.monster_num):
            card_info=self.read_monster[n]
            book=xlwt.Workbook(encoding='utf-8',style_compression=0)
            for m in xrange(len(self.res1)):
                sheet=book.add_sheet(self.res1[m],cell_overwrite_ok=True)
                sheet.write(0,0,'id')
                sheet.write(1,0,'name')
                sheet.write(0,1,card_info['id'])
                sheet.write(1,1,card_info['name'])
            book.save(r'd:\first.xls')
if __name__=="__main__":
    test01=hero_card()
    test01.get_card_info()