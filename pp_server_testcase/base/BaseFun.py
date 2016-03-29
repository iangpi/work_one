#coding:utf-8
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import sys,os,unittest,time
reload(sys)
sys.setdefaultencoding('utf-8')#避免出现乱码

class Base(unittest.TestCase):
    #预备唱
    def setUp(self):
        print 'start test'
        self.ff=webdriver.Firefox()
        #self.ff.refresh()
        self.ff.maximize_window()
        self.ff.get(r'http://awsbj-openmanagement.xingyunzhi.cn/developer-user/login')
    #收！
    def tearDown(self):
        print 'end test'
        self.ff.quit()
    #封装定位方法
    def by_id(self,the_id):
        return self.ff.find_element_by_id(the_id)
    def by_classname(self,the_classname):
        return self.ff.find_element_by_class_name(the_classname)
    def by_xpath(self,the_xpath):
        return self.ff.find_element_by_xpath(the_xpath)
    #封装用户名和密码输入
    def test_login(self):
        "登录测试"
        self.by_id('username').clear()
        self.by_id('username').send_keys('wxg')
        self.by_id('password').clear()
        self.by_id('password').send_keys('wxg')
        self.by_id('submit').click()
        self.assertEqual('搜索',self.by_xpath(".//*[@id='content']/div/div/div/div[2]/div[2]/div/a").text)
if __name__=='__main__':
    unittest.main()
    #shift+f9 to run testcase
    # testunit=unittest.TestSuite()
    # testunit.addTest(Base("test_login"))
    # test_time=time.strftime("%Y_%m_%d_%H_%M_%S")
    # #save_path=os.path.abspath(r"E:\mypython\pengpeng\PPTestReport\.")#最后的report不是路径，是要创建的报告的文件名,可以指定都集中放在哪里
    # filename='./'+test_time+'result.html'#存放于当前目录
    # print filename
    # fp=open(filename,'wb')
    # runner=HTMLTestRunner(stream=fp,
    #                       title='登录case',
    #                       description='case执行情况'
    #                       )
    # runner.run(testunit)
    # fp.close()