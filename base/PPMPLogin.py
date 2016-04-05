#coding:utf-8
from selenium import webdriver
from PPMPChoseBrowser import Chose_Browser
import sys,os
#避免出现乱码
reload(sys)
sys.setdefaultencoding('utf-8')
#跨文件引用
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
el_username='username'
el_password='password'
el_submit='submit'

class Login(object):
    def LoginSuccess(self,username,password):
        the_browser=Chose_Browser()#实例化打开浏览器类
        the_browser.which_Browser('ff')
        the_browser.open_Browser(r'http://awsbj-openmanagement.xingyunzhi.cn/developer-user/login')
if __name__=="__main__":
    Login().LoginSuccess('wxg','wxg')

