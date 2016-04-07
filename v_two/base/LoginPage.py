#coding:utf-8
from selenium import webdriver
from Page import Base
import sys,os,time

reload(sys)
sys.setdefaultencoding('utf-8')#避免出现乱码
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#跨文件引用
sys.path.insert(0,parentdir)
url=r"http://awsbj-openmanagement.xingyunzhi.cn/developer-user/login"
class LoginSuccess(object):
    #成功登录方法
    def loginsuccess(self,el_username,el_password,el_submit,the_u,the_p):
        dr=Base(webdriver.Firefox())#实例化类
        dr.open(url)
        dr.by_id(el_username).clear()
        dr.by_id(el_username).send_keys(the_u)
        dr.by_id(el_password).clear()
        dr.by_id(el_password).send_keys(the_p)
        dr.by_id(el_submit).click()
        try:
            test_el=dr.by_xpath(".//*[@id='content']/div/div/div/div[2]/div[2]/div/a").text
            assert test_el==u'搜1索'
        except:
            print 'assert fail'
        else:
            print 'assert pass'
if __name__=="__main__":
    mytest=LoginSuccess()
    mytest.loginsuccess('username','password','submit','wxg','wxg')

