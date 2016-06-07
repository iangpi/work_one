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

    def all_cards_skill(self):
        cards_skill=[]#每三个id一样的放到一个小list里，最后放到这个cards_skill里
        for n in xrange(self.unlock_skill_num):
            #在unlock表里，如果一张卡的id和第三张的id相等，那么1，2，3张分别是主动，被动，天赋
            card_skill=[]
            if self.unlock_skill_num-n>3 and self.read_unlock_skill[n]['id']==self.read_unlock_skill[n+2]['id']:
                card_skill.append(self.read_unlock_skill[n])
                card_skill.append(self.read_unlock_skill[n+1])
                card_skill.append(self.read_unlock_skill[n+2])
                cards_skill.append(card_skill)
            elif self.unlock_skill_num-n==3:
                card_skill.append(self.read_unlock_skill[-3])
                card_skill.append(self.read_unlock_skill[-2])
                card_skill.append(self.read_unlock_skill[-1])
                cards_skill.append(card_skill)
            else:
                pass
        return cards_skill

    def get_info_by_id(self,the_id,the_el):
        for n in xrange(self.monster_num):
            if self.read_monster[n]['id']==the_id:
                res=self.read_monster[n][the_el]
        return res

    #深入抽取信息 and 写入表格
    def write_info_to_excel(self):
        #初始化，实例化类的方法
        mycalss=hero_card()
        fun1=mycalss.all_cards_id()
        fun2=mycalss.all_cards()
        fun3=mycalss.all_cards_skill()
        #参数化数据存放
        row_1_part_1=['编号','名字','输出类型','子类型','卡牌类型','解锁等级','可收集否','可移动否','形象','描述','品质','尺寸','速度']
        row_2_part_1=['id','name','type','subType','unitType','unlockLevel','collectable','moveable','avatarId','desc','quality','size','speed']
        row_1_part_2=['编号','主动技能',
                      '1级解锁技能','技能等级',
                      '4级解锁技能','技能等级',
                      '7级解锁技能','技能等级',
                      '10级解锁技能','技能等级',
                      '12级解锁技能','技能等级',
                      '14级解锁技能','技能等级',
                      '16级解锁技能','技能等级',
                      '18级解锁技能','技能等级',
                      '20级解锁技能','技能等级'
                      ]
        row_2_part_2=['id','type',
                      'skillId1','skillLevel1',
                      'skillId4','skillLevel4',
                      'skillId7','skillLevel7',
                      'skillId10','skillLevel10',
                      'skillId12','skillLevel12',
                      'skillId14','skillLevel14',
                      'skillId16','skillLevel16',
                      'skillId18','skillLevel18',
                      'skillId20','skillLevel20'
                      ]
        #新建并打开一个表格(解决思路：先新建表格，再写入数据，数据从哪里来，根据id的唯一性，查询而来）
        book=xlwt.Workbook(encoding='utf-8',style_compression=0)
        #卡牌表有多长，就新建多少个sheet分页，并且用卡牌表中的名字命名分页
        for n in xrange(len(fun1)):#直接实例化自己类里的方法直接用
            sheet_name=str(fun1[n])
            sheet=book.add_sheet(sheet_name,cell_overwrite_ok=True)
            sheet.write(0,0,'基本信息')
            sheet.write(1,1,'')
            num_1=len(row_1_part_1)
            for m in xrange(num_1):
                sheet.write(m+1,0,row_1_part_1[m])
                sheet.write(m+1,1,str(fun2[n][row_2_part_1[m]]))

            #下面的+2+3是为了横向写三列，分别是主动，被动，天赋
            sheet.write(num_1+2,0,'主动技能')
            sheet.write(num_1+2,1,'')
            sheet.write(num_1+2,2,'被动技能')
            sheet.write(num_1+2,3,'')
            sheet.write(num_1+2,4,'天赋技能')
            sheet.write(num_1+2,5,'')
            #获取遍历的次数
            num_2=len(row_1_part_2)
            #遍历主动技能，写入
            for w in xrange(num_2):
                sheet.write(w+num_1+3,0,row_1_part_2[w])
                sheet.write(w+num_1+3,1,str(fun3[n][0][row_2_part_2[w]]))
            #遍历被动技能，写入
            for x in xrange(num_2):
                sheet.write(x+num_1+3,2,row_1_part_2[x])
                sheet.write(x+num_1+3,3,str(fun3[n][1][row_2_part_2[x]]))
            #遍历天赋技能，写入
            for y in xrange(num_2):
                sheet.write(y+num_1+3,4,row_1_part_2[y])
                sheet.write(y+num_1+3,5,str(fun3[n][2][row_2_part_2[y]]))
        #写入过后，保存表格
        book.save(r'D:\mygit\work_one\zhanqi\report\user_cards.xls')

if __name__=="__main__":
    test01=hero_card()
    test01.write_info_to_excel()
    #确保技能表除以3的结果恒等于怪物表的里怪物的数量
    print len(test01.all_cards_skill())
    print test01.monster_num