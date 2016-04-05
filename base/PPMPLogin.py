#coding:utf-8
from selenium import webdriver
from PPMPChoseBrowser import The_Driver
from PPMPFind_el import Find_Element
import sys,os

reload(sys)
sys.setdefaultencoding('utf-8')#避免出现乱码
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#跨文件引用
sys.path.insert(0,parentdir)

el_username='username'
el_password='password'
el_submit='submit'

my_driver=The_Driver()#实例化类
my_el=Find_Element()

class Login(object):
    def LoginSuccess(self,username,password,browser_name,the_url):
        my_driver.open_browser(browser_name)


if __name__=="__main__":
    Login().LoginSuccess('wxg','wxg')

