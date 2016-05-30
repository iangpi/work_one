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
        #读怪物json
        self.monster_file=file(path_monster)
        self.read_monster=json.load(self.monster_file)
        self.monster_num=len(self.read_monster)
        print ('怪物总数:'),self.monster_num

        #抽取出来玩家的卡牌，并数序排列
        self.user_cards=[]
        for n in xrange(self.monster_num):
            if self.read_monster[n]['collectable']==1:
                self.user_cards.append(self.read_monster[n]['id'])
        self.res1=sorted(self.user_cards)

        #抽取出来怪物的卡牌，并顺序排列
        self.monster_cards=[]
        for n in xrange(self.monster_num):
            if self.read_monster[n]['collectable']==0:
                self.monster_cards.append(self.read_monster[n]['id'])
        self.res2=sorted(self.monster_cards)


        #读skill的json
        self.skill_file=file(path_skill)
        self.read_skill=json.load(self.skill_file)
        self.skill_num=(len(self.read_skill))

        #读unlock_skill的json
        self.unlock_skill_file=file(path_unlockSkill)
        self.read_unlock_skill=json.load(self.unlock_skill_file)
        self.unlock_skill_num=len(self.read_unlock_skill)

    def get_card_info(self):
        for n in xrange(self.monster_num):
            self.card_info=self.read_monster[n]
        return self.card_info
    #深入抽取信息 and 写入表格
    def write_in_excel(self):
        #新建并打开一个表格(解决思路：先新建表格，再写入数据，数据从哪里来，根据id的唯一性，查询而来）
        book=xlwt.Workbook(encoding='utf-8',style_compression=0)
        #卡牌表有多长，就新建多少个sheet分页，并且用卡牌表中的名字命名分页
        for n in xrange(len(self.res1)):
            print self.res1[0]
            sheet=book.add_sheet(self.res1[n],cell_overwrite_ok=True)
            sheet.write(0,1,(self.res1[n]['id']))
        #保存表格
        # book.save(r'd:\first.xls')
if __name__=="__main__":
    test01=hero_card()
    test01.write_in_excel()