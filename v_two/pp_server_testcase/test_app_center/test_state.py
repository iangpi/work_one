#coding:utf-8
from HTMLTestRunner import HTMLTestRunner
import unittest,time,sys,os
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)


class State(unittest.TestCase):
    def not_check(self):
        self.assertEqual()