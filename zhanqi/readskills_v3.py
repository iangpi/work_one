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
        self.user_cards=[]
        self.monster_cards=[]

    def all_usercards(self):
        #抽取出来玩家的卡牌，并数序排列
        for n in xrange(self.monster_num):
            if self.read_monster[n]['collectable']==1:
                self.user_cards.append(self.read_monster[n]['id'])
                self.res1=sorted(self.user_cards)
        return self.res1

    def all_monstercards(self):
        #抽取出来怪物的卡牌，并顺序排列
        for n in xrange(self.monster_num):
            if self.read_monster[n]['collectable']==0:
                self.monster_cards.append(self.read_monster[n]['id'])
                self.res2=sorted(self.monster_cards)
        return self.res2

    def get_info_by_id(self,the_id,the_el):
        for n in xrange(self.monster_num):
            if self.read_monster[n]['id']==the_id:
                res=self.read_monster[n][the_el]
        return res

    #深入抽取信息 and 写入表格
    def write_in_excel(self):
        #新建并打开一个表格(解决思路：先新建表格，再写入数据，数据从哪里来，根据id的唯一性，查询而来）
        book=xlwt.Workbook(encoding='utf-8',style_compression=0)
        #卡牌表有多长，就新建多少个sheet分页，并且用卡牌表中的名字命名分页
        for n in xrange(len(self.res1)):
            sheet=book.add_sheet(self.res1[n],cell_overwrite_ok=True)
            sheet.write(0,1,str((hero_card().get_info_by_id('monster013','name'))))
        #保存表格
        book.save(r'd:\first.xls')

if __name__=="__main__":
    test01=hero_card()
    print test01.all_usercards()
    print test01.all_monstercards()
    print test01.get_info_by_id('monster013','name')
    test01.write_in_excel()