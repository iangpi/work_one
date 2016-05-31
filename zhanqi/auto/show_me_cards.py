#coding:utf-8
from selenium import webdriver
import json
import os
import time
print time.ctime()
#获取怪物表
path_monster=os.path.abspath(r"D:\mygit\work_one\zhanqi\myjson\monster.json")
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
test_address=r"http://tactics.xingyunzhi.cn/delta/admin.html"
need_nums=1000


#nick_name='Houlin'
#nick_name=u'奇怪的选手'
#nick_name=u'不大不小超'
nick_name=u'葫芦娃二娃'
#nick_name='shunia'#包子

#dr=webdriver.Firefox()
#无界面浏览器
phantomjs_path=os.path.abspath(r"C:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe")
dr=webdriver.PhantomJS(phantomjs_path)
dr.get(test_address)
time.sleep(1)

#查找用户
dr.find_element_by_id('server_id').clear()
dr.find_element_by_id('server_id').send_keys('7001')
dr.find_element_by_id('nick_name').send_keys(nick_name)
dr.find_element_by_xpath(".//*[@id='query_user']/p[5]/input").click()
time.sleep(1)
dr.find_element_by_id('coin').clear()
dr.find_element_by_id('coin').send_keys('100000')
dr.find_element_by_id('cash').clear()
dr.find_element_by_id('cash').send_keys('100000')
dr.find_element_by_xpath(".//*[@id='features']/p[4]/input[3]").click()

#遍历玩家卡牌表，挨个添加
for num in xrange(len(user_cards)):
    dr.find_element_by_xpath(".//*[@id='unit_id']").send_keys(user_cards[num])
    dr.find_element_by_xpath(".//*[@id='unit_count']").send_keys(need_nums)
    dr.find_element_by_xpath(".//*[@id='features']/p[6]/input[3]").click()
    time.sleep(0.5)
    #断言一下，发送卡牌失败报错，断言发送失败的文字
    try:
        get_text=dr.find_element_by_xpath(".//*[@id='query_result']").text
        hope_text1='ok'
        hope_text2='count'
        assert (hope_text1 in get_text) and (hope_text2 in get_text)
    except:
        print 'send cards failed'
    else:
        pass
        print user_cards[num],'has added',need_nums
    time.sleep(0.5)
    dr.find_element_by_id('unit_id').clear()
    dr.find_element_by_xpath(".//*[@id='unit_count']").clear()

dr.quit()
monsters_file.close()#别忘记关闭json文件，否则没法编辑
print time.ctime()