#coding:utf-8
import sys
sys.path.append("./Page")
sys.path.append("./Loginpage")
sys.path.append("./Variables")
import os
import time
from base import Variables

#避免出现乱码
reload(sys)
sys.setdefaultencoding('utf-8')
#跨文件引用


class App_Center_Base(object):
    def app_center_page(self):
        return Variables.app_center_url