#coding:utf-8
from selenium import webdriver
import json
import os
import time
print time.ctime()
#获取怪物表
path_monster=os.path.abspath(r"D:\mygit\work_one\zhanqi\myjson\monster_old.json")
monsters_file=file(path_monster)
search_monsters=json.load(monsters_file)
monsters_num=len(search_monsters)
print ('当前英雄卡牌数量：'),monsters_num
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
user_cards.sort()
monster_cards.sort()
print user_cards
print monster_cards

#用户名字和想要卡牌数量参数化
myd={'7001_id':'7001',
     '4001_id':'4001',
     '7001_address':'http://tactics.xingyunzhi.cn/delta/admin.html',
     '4001_address':'http://tactics.xingyunzhi.cn/staging/admin.html'
     }
card_nums=5000
coin_nums=999950
cash_nums=1000000
#nick_name='Houlin'
#nick_name=u'奇怪的选手'
#nick_name=u'不大不小超'
nick_name=u'葫芦娃二娃'
#nick_name='shunia'#包子

#dr=webdriver.Firefox()
#无界面浏览器
phantomjs_path=os.path.abspath(r"C:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe")
dr=webdriver.PhantomJS(phantomjs_path)
dr.get(myd[r'7001_address'])
time.sleep(0.5)

#查找用户
dr.find_element_by_id('server_id').clear()
dr.find_element_by_id('server_id').send_keys(myd['7001_id'])
dr.find_element_by_id('nick_name').send_keys(nick_name)
dr.find_element_by_xpath(".//*[@id='query_user']/p[5]/input").click()
time.sleep(1)
get_res=dr.find_element_by_xpath(".//*[@id='query_result']").text
print len(get_res)
# print len(get_res)
# right_res={"status":"ok","users":{"uid":"574ea818b80327025723feae","nickName":"葫芦娃二娃"}}
# print len(right_res)
# wrong_res={"status":"ok","users":[{"uid":"574ea818b80327025723feae","nickName":"葫芦娃二娃"},{"uid":"574eb7b2b80327025723febc","nickName":"葫芦娃二娃"}]}
#判断一下搜索出来后，当前是没有帐号还是有多个帐号
if len(get_res)<100:
    dr.find_element_by_id('coin').clear()
    dr.find_element_by_id('coin').send_keys(coin_nums)
    dr.find_element_by_id('cash').clear()
    dr.find_element_by_id('cash').send_keys(cash_nums)
    dr.find_element_by_xpath(".//*[@id='features']/p[4]/input[3]").click()
else:
    print ('请确认当前游戏中有几个相同昵称的帐号')
cards_list=['monster003',
            'monster004',
            'monster005',
            'monster006',
            'monster007',
            'monster009',
            'monster011',
            'monster012',
            'monster013',
            'monster016',
            'monster018',
            'monster027',
            'monster034',
            'monster035',
            'monster038',
            'monster040',
            'monster042',
            'monster044',
            'monster065'
            ]
#遍历玩家卡牌表，挨个添加
for n in xrange(len(cards_list)):
    dr.find_element_by_xpath(".//*[@id='unit_id']").send_keys(cards_list[n])
    dr.find_element_by_xpath(".//*[@id='unit_count']").send_keys(card_nums)
    dr.find_element_by_xpath(".//*[@id='features']/p[6]/input[3]").click()
    time.sleep(0.3)
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
        print cards_list[n],'has added',card_nums
    time.sleep(0.5)
    dr.find_element_by_id('unit_id').clear()
    dr.find_element_by_xpath(".//*[@id='unit_count']").clear()

dr.quit()
monsters_file.close()#别忘记关闭json文件，否则没法编辑
print time.ctime()