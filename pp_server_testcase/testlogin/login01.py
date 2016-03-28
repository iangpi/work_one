#coding:utf-8
from HTMLTestRunner import HTMLTestRunner
import unittest,time,sys,os
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from base import BaseFun01
class test_login01(unittest.TestCase):
    def setUp(self):
        print ('test start')
    "登陆测试"
    def test_login_suess(self):
        www=BaseFun01.Base()
        "继承了BaseFun01.py下，base类里的各种方法，传入参数直接用"
        www.open_browser(r"http://awsbj-openmanagement.xingyunzhi.cn/developer-user/login")#打开网址
        www.login('wxg','wxg')#输入用户名和密码
        el=www.by_xpath(".//*[@id='content']/div/div/div/div[2]/div[2]/div/a").text#提取要断言的文字
        self.assertEqual('搜索',el)#断言是否相等
        time.sleep(2)
        www.close_browser()
    def tearDown(self):
        print ('test end')
if __name__=="__main__":
    testunit=unittest.TestSuite()
    testunit.addTest(test_login01("test_login_suess"))
    test_time=time.strftime("%Y_%m_%d_%H_%M_%S")
    save_path=os.path.abspath(r"E:\mypython\pengpeng\pp_test_report\testreport")
    filename=save_path+test_time+'.html'
    print filename
    htmlreprot=open(filename,'wb')
    runner=HTMLTestRunner(stream=htmlreprot,
                          title='登录case',
                          description='case执行情况'
                         )
    runner.run(testunit)
    htmlreprot.close()