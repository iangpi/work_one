#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
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
'''
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
'''


#跨文件引用其他文件的变量
import os,sys
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#跨文件引用
sys.path.insert(0,parentdir)
from base import Variables
print Variables.the_url
print Variables.the_test_url


'''
#打印元素的文字，用作断言
from selenium import webdriver
import time
ff=webdriver.Firefox()
ff.get(r"http://www.baidu.com")
a=ff.find_element_by_xpath(".//*[@id='u1']/a[1]").text
assert a=='糯米'
time.sleep(3)
ff.close()
'''