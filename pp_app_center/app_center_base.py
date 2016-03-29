#coding:utf-8
from selenium import webdriver
import os,sys,time
from pp_server_testcase.base import BaseFun01
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
class App_Center_Base(object):
    def app_center_url(self):
        return 'http://awsbj-openmanagement.xingyunzhi.cn/app-bak/get-app-list'


if __name__=="__mian__":
    www=BaseFun01.Base()#类的实例化
    www.open_browser(r'http://awsbj-openmanagement.xingyunzhi.cn/developer-user/login')#打开网址
    www.login('wxg','wxg')#用户名和密码传参数

