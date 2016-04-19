#coding:utf-8
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
def creat_suite():
    testunit=unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir=r"D:\mygit\work_one\v_3\app_center"
    #定义discover方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,
                                                 pattern='test*.py',
                                                 top_level_dir=None
                                                 )
    for test_case in discover:
        print test_case,
        testunit.addTest(test_case)
    return testunit

test_time=time.strftime("%Y-%m-%d %H_%M_%S")
# 家里的存放地址
# save_path=os.path.abspath(r"E:\mypython\pengpeng\pp_test_report\\")
# 公司的存放地址
save_path=r'D:\mygit\work_one\v_3\pp_test_report\datebase_testreport\\'
filename=save_path+test_time+'result.html'
fp=file(filename,'wb')
runner=HTMLTestRunner(stream=fp,
                      title='数据中心测试报告',
                      description='设置类,子项目测试报告'
                      )
if __name__=="__main__":
    alltestnames=creat_suite()
    runner.run(alltestnames)
    fp.close()