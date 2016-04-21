#coding:utf-8
'''
复习下if __name__=='__main__':
def b(x,y):
    return x+y
if __name__=='__main__':
    print b(1,2)
'''
'''
复习下如何用selenium启动chrome，记得要下载一个chromedriver.exe的驱动
from selenium import webdriver
import os,time
chromepath=os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
ch=webdriver.Chrome(chromepath)
ch.refresh()
ch.get(r"http://www.baidu.com")
time.sleep(2)
ch.quit()
'''
#做一个关于启动不同浏览器的方法
"""
from selenium import webdriver
import os,time
def which_browser(br_name):
    chromepath=os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    if br_name=='ff':
        ff=webdriver.Firefox()
        ff.get(r"http://www.baidu.com")
        time.sleep(3)
        ff.quit()
    elif br_name=='ch':
        ch=webdriver.Chrome(chromepath)
        ch.get(r"http://www.baidu.com")
        time.sleep(3)
        ch.quit()
    else:
        print (u'熊孩子别乱写,请输入"ff 或者 ch"')

if __name__=="__main__":
    which_browser('12')
"""

'''
#跨文件引用其他文件的变量
import os,sys
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#跨文件引用
sys.path.insert(0,parentdir)
from base import Variables
print Variables.the_url
print Variables.the_test_url
'''

'''
#打印元素的文字，用作断言
from selenium import webdriver
import time
ff=webdriver.Firefox()
ff.get(r"http://www.baidu.com")
a=ff.find_element_by_xpath(".//*[@id='u1']/a[1]").text
assert a=='糯米'
time.sleep(3)
ff.quit ()
'''

'''
from selenium import webdriver
driver=webdriver.Firefox()
driver.switch_to_alert().accept()#好像这种是不推荐的写法,所以上面有个横线
driver.switch_to.alert().accept()
'''

'''
#跨文件引用的另一种办法（非平级引用）
import sys
sys.path.append(r"D:\mygit\work_one\v_two\base")
import Variables
print Variables.the_real_url
'''

'''
#如果是平级引用，可以这样写
import sys
sys.path.append("./base")
import test0002
print test0002.a
'''

'''退出登录后，返回登陆页面，获取登录页面tile
from selenium import webdriver
import time
ff=webdriver.Firefox()
ff.get(r"http://awsbj-openmanagement.xingyunzhi.cn/developer-user/index")
ff.find_element_by_id('username').send_keys('wxg')
ff.find_element_by_id('password').send_keys('wxg')
ff.find_element_by_id('submit').click()
ff.find_element_by_xpath('html/body/div[1]/div/div/button').click()
ff.find_element_by_xpath('html/body/div[1]/div/div/ul/li[2]/a').click()
time.sleep(2)
print ff.title
'''

'''
#测试打印title的type
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class mytitle():
    def the_title(self):
        ff=webdriver.Firefox()
        ff.get(r"http://www.baidu.com")
        baidu_title=ff.title
        print type(baidu_title)
        ff.quit()
        return baidu_title
if __name__=="__main__":
    test01=mytitle()
    test01.the_title()
'''


'''对list和dict格式的读取
a=[
 {"name": "ONE","cities": {"city": ["1", "2"]}},
 ]
print a[0]
print a[0]['cities']
print a[0]['cities']['city']
print a[0]['cities']['city'][0]
'''


a='asdasda"asda\'sd\'asd"'
print a