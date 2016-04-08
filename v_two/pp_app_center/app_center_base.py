#coding:utf-8
import sys
import os
import time
#跨文件引用

parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from base import Variables

print Variables.the_real_url

# #避免出现乱码
# reload(sys)
# sys.setdefaultencoding('utf-8')
# #跨文件引用
#
#
# class App_Center_Base(object):
#     def app_center_page(self):
#         return Variables.app_center_url