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

    def all_usercards(self):
        #抽取出来玩家的卡牌
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
        #抽取玩家卡牌id，
    def all_usercards_id(self):
        cards_id=[]
        for n in xrange(self.monster_num):
            if self.read_monster[n]['collectable']==1:
                cards_id.append(self.read_monster[n]['id'])
        return cards_id

    def all_usercards_skill(self):
        cards_skill=[]
        for n in xrange(self.unlock_skill_num):
            if self.read_unlock_skill[n]['id'] in hero_card().all_usercards_id():
                    cards_skill.append(self.read_unlock_skill[n])
        return cards_skill

    def all_monstercards(self):
        #抽取出来怪物的卡牌，
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
    def write_info_to_excel(self):
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
            row_1=['编号','名字','输出类型','子类型','卡牌类型','解锁等级','可收集否','可移动否','形象','描述','品质','尺寸','速度']
            row_2=['id','name','type','subType','unitType','unlockLevel','collectable','moveable','avatarId','desc','quality','size','speed']
            num=len(row_1)
            for m in xrange(num):
                sheet.write(m,0,row_1[m])
                sheet.write(m,1,str(fun2[n][row_2[m]]))
        #保存表格
        book.save(r'D:\mygit\work_one\zhanqi\report\user_cards.xls')



if __name__=="__main__":
    test01=hero_card()
    # for n in xrange(len(test01.all_usercards())):
    #     print '玩家卡牌：',test01.all_usercards()[n]['id']
    # for n in xrange(len(test01.all_monstercards())):
    #     print 'npc卡牌：',test01.all_monstercards()[n]['name']
    test01.write_info_to_excel()
    print test01.all_usercards_skill()
    print len(test01.all_usercards_skill())