#coding:utf-8
from HTMLTestRunner import HTMLTestRunner
import unittest,time,sys,os
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from pp_server_testcase.base import BaseFun
class test_login01(unittest.TestCase):
    """测试说明1"""
    def setUp(self):
        print ('test start')
    def test_login_suess(self):
        """测试说明2"""
        www=BaseFun.Base()
        "继承了BaseFun01.py下，base类里的各种方法，传入参数直接用"
        www.open_browser_with_firefox(r'http://awsbj-openmanagement.xingyunzhi.cn/developer-user/login')#打开网址
        www.login('wxg','wxg')#用户名和密码传参数
        el=www.by_xpath(".//*[@id='content']/div/div/div/div[2]/div[2]/div/a").text#提取要断言的文字
        self.assertEqual('搜索',el)#断言
        time.sleep(2)
        www.close_browser()
    def tearDown(self):
        print ('test end')
if __name__=="__main__":
    testunit=unittest.TestSuite()
    testunit.addTest(test_login01("test_login_suess"))
    test_time=time.strftime("%Y_%m_%d_%H_%M_%S")
    #save_path=os.path.abspath(r"E:\mypython\pengpeng\pp_test_report\testreport")#家里的存放地址
    save_path=os.path.abspath(r"D:\mygit\work_one\pp_test_report\testreport")#公司的存放地址
    filename=save_path+test_time+'.html'
    print filename
    htmlreprot=open(filename,'wb')
    runner=HTMLTestRunner(stream=htmlreprot,
                          title='这是标题',
                          description='这是测试报告详细内容'
                          )
    runner.run(testunit)
    htmlreprot.close()