#coding:utf-8
from PPMPChoseBrowser import The_Driver
from PPMPFind_el import Find_Element
import sys,os,time

reload(sys)
sys.setdefaultencoding('utf-8')#避免出现乱码
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#跨文件引用
sys.path.insert(0,parentdir)

the_driver=The_Driver()#实例化类
the_el=Find_Element()
browser_name='ff'
class Login(object):
    def loginsuccess(self,u,p):
        dr=the_driver.the_browser(browser_name)
        dr.get(the_url)
        the_el.by_id(el_username).clear()
        the_el.by_id(el_username).send_keys(u)
        the_el.by_id(el_password).clear()
        the_el.by_id(el_password).send_keys(p)
        the_el.by_id(el_submit).click()
if __name__=="__main__":
    el_username='username'#下面是用户名，密码和提交按钮的变量
    el_password='password'
    el_submit='submit'

    the_url=r"http://awsbj-openmanagement.xingyunzhi.cn/developer-user/login"

    Login().loginsuccess('wxg','wxg')
    time.sleep(3)

    assert u'碰碰管理平台'==the_el.by_xpath("html/body/div[1]/div/a/span")

