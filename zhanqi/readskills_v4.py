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
        #print ('怪物总数:'),self.monster_num

    def all_usercards(self):
        #抽取出来玩家的卡牌，并数序排列
        user_cards=[]
        for n in xrange(self.monster_num):
            if self.read_monster[n]['collectable']==1:
                user_cards.append(self.read_monster[n])
        return user_cards
        #抽取玩家卡牌名字，用作给表格建立分页用
    def all_usercards_name(self):
        cards_name=[]
        for n in xrange(self.monster_num):
            if self.read_monster[n]['collectable']==1:
                cards_name.append(self.read_monster[n]['name'])
        return cards_name

    def all_usercards_id(self):
        cards_id=[]
        for n in xrange(self.monster_num):
            if self.read_monster[n]['collectable']==1:
                cards_id.append(self.read_monster[n]['id'])
        return cards_id

    def all_monstercards(self):
        #抽取出来怪物的卡牌，并顺序排列
        monster_cards=[]
        for n in xrange(self.monster_num):
            if self.read_monster[n]['collectable']==0:
                monster_cards.append(self.read_monster[n])
        return monster_cards

    def get_info_by_id(self,the_id,the_el):
        for n in xrange(self.monster_num):
            if self.read_monster[n]['id']==the_id:
                res=self.read_monster[n][the_el]
        return res

    #深入抽取信息 and 写入表格
    def write_in_excel(self):
        #初始化，实例化类的方法
        mycalss=hero_card()
        fun1=mycalss.all_usercards_id()
        fun2=mycalss.all_usercards()
        #新建并打开一个表格(解决思路：先新建表格，再写入数据，数据从哪里来，根据id的唯一性，查询而来）
        book=xlwt.Workbook(encoding='utf-8',style_compression=0)
        #卡牌表有多长，就新建多少个sheet分页，并且用卡牌表中的名字命名分页
        for n in xrange(len(fun1)):#直接实例化自己类里的方法直接用
            sheet_name=str(fun1[n])
            sheet=book.add_sheet(sheet_name,cell_overwrite_ok=True)
            sheet.write(0,0,'id')
            sheet.write(1,0,'名字')
            sheet.write(2,0,'单位输出类型')
            sheet.write(3,0,'单位子类型')
            sheet.write(4,0,'卡牌类型')
            sheet.write(5,0,'解锁等级')
            sheet.write(6,0,'可收集')
            sheet.write(7,0,'可移动')
            sheet.write(8,0,'单位形象')
            sheet.write(9,0,'单位描述')
            sheet.write(10,0,'单位品质')
            sheet.write(11,0,'单位尺寸')
            sheet.write(12,0,'速度')

            sheet.write(0,1,str(fun2[n]['id']))
            sheet.write(1,1,str(fun2[n]['name']))
            sheet.write(2,1,str(fun2[n]['type']))
            sheet.write(3,1,str(fun2[n]['subType']))
            sheet.write(4,1,str(fun2[n]['unitType']))
            sheet.write(5,1,str(fun2[n]['unlockLevel']))
            sheet.write(6,1,str(fun2[n]['collectable']))
            sheet.write(7,1,str(fun2[n]['moveable']))
            sheet.write(8,1,str(fun2[n]['avatarId']))
            sheet.write(9,1,str(fun2[n]['desc']))
            sheet.write(10,1,str(fun2[n]['quality']))
            sheet.write(11,1,str(fun2[n]['size']))
            sheet.write(12,1,str(fun2[n]['speed']))
        #保存表格
        book.save(r'd:\first.xls')

if __name__=="__main__":
    test01=hero_card()
    # for n in xrange(len(test01.all_usercards())):
    #     print '玩家卡牌：',test01.all_usercards()[n]['id']
    # for n in xrange(len(test01.all_monstercards())):
    #     print 'npc卡牌：',test01.all_monstercards()[n]['name']
    test01.write_in_excel()