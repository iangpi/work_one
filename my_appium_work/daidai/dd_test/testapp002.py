#coding:utf-8
import os,sys
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#跨文件引用
sys.path.insert(0,parentdir)
from dd_base import DD_Data

print DD_Data.elements().home_els('商店')