#coding:utf-8
from selenium import webdriver
import json
import os
import time
#获取怪物表
path_monster=os.path.abspath(r"D:\mygit\work_one\zhanqi\monster.json")
monsters_file=file(path_monster)
search_monsters=json.load(monsters_file)
monsters_num=len(search_monsters)
print monsters_num
#建立2个空list，接受玩家卡牌和电脑卡牌的id
user_cards=[]
monster_cards=[]
for n in xrange(monsters_num):
    # print search_monsters[n]['id']
    # print search_monsters[n]['collectable']
    if search_monsters[n]['collectable']==1:
        user_cards.append(search_monsters[n]['id'])
    else:
        monster_cards.append(search_monsters[n]['id'])
print user_cards
print monster_cards

#用户名字和想要卡牌数量参数化
need_nums=10
nick_name=u'不大不小超'
#nick_name=u'奇怪的选手'

#无界面浏览器
phantomjs_path=os.path.abspath(r"C:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe")
dr=webdriver.PhantomJS(phantomjs_path)
dr.get(r"http://tactics.xingyunzhi.cn:4000/admin.html")
time.sleep(1)

#查找用户
dr.find_element_by_id('nick_name').send_keys(nick_name)
dr.find_element_by_xpath('html/body/p[4]/input').click()
time.sleep(1)

#遍历玩家卡牌表，挨个添加
for num in xrange(len(user_cards)):
    dr.find_element_by_id('unit_id').send_keys(user_cards[num])
    dr.find_element_by_xpath(".//*[@id='unit_count']").send_keys(need_nums)
    time.sleep(1)
    dr.find_element_by_xpath(".//*[@id='features']/p[6]/input[3]").click()
    time.sleep(1)
    print user_cards[num],'has added',10
    dr.find_element_by_id('unit_id').clear()
    dr.find_element_by_xpath(".//*[@id='unit_count']").clear()