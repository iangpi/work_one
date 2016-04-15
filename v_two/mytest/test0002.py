#coding:utf-8
import sys
sys.path.append('./mytest')
import test0001
print test0001.d['a']

    # testunit=unittest.TestSuite()
    # testunit.addTest(BasePage("test_login_add_apk_bak"))
    # test_time=time.strftime("%Y_%m_%d_%H_%M_%S")
    # save_path=os.path.abspath(r"D:\mygit\work_one\pp_test_report\testreport")#公司的存放地址
    # filename=save_path+test_time+'.html'
    # print filename
    # htmlreprot=open(filename,'wb')
    # runner=HTMLTestRunner(stream=htmlreprot,
    #                       title='这是标题',
    #                       description='这是测试报告详细内容'
    #                       )
    # runner.run(testunit)
    # htmlreprot.close()