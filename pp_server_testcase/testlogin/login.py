#coding:utf-8
from HTMLTestRunner import HTMLTestRunner
import unittest,time,sys,os
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
#sys.path.append(r"..")#从base文件夹到BaseFun.py文件。
from base import BaseFun

if __name__=="__main__":
    testunit=unittest.TestSuite()
    testunit.addTest(BaseFun.Base("test_login"))
    test_time=time.strftime("%Y_%m_%d_%H_%M_%S")
    #save_path=os.path.abspath(r"E:\mypython\pengpeng\pp_test_report\testreport")#家里的存放地址
    save_path=os.path.abspath(r"D:\mygit\work_one\pp_test_report\testreport")#公司的存放地址
    filename=save_path+test_time+'result.html'
    print filename
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,
                          title='登录case',
                          description='case执行情况'
                         )
    runner.run(testunit)
    fp.close()



