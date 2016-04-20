#coding:utf-8
import urllib
import urllib2
import unittest

class TestCode(unittest.TestCase):
    def setUp(self):
        self.url=r"http://api.douban.com/v2/boob/user/ahbei/collections"
        self.data={'status':'read','rating':'3','tag':'小说'}
        self.data=urllib.urlencode(self.data)
        self.url2=urllib2.Request(self.url,self.data)
        self.response=urllib2.urlopen(self.url2)
        self.api_content=self.response.read()
        #read()返回的结果是str，不方便操作，使用内置函数eval专程dict
        self.content_json=eval(self.api_content)
    def test_code(self):
        book_count=self.content_json.get('total')
        self.assertEqual()