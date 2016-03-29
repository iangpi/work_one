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
