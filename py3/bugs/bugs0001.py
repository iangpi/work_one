'''
非常简单的一小段代码
import urllib    
def getHtml(url):  
    page = urllib.urlopen(url).read()  
    html=page.read()  
    return html  
  
url="http://tieba.baidu.com/p/4040087257/"  
html=getHtml(url)  

print(html)  
报错：
    “AttributeError: 'module' object has no attribute 'urlopen'”
原因是Python3里的urllib模块已经发生改变，此处的urllib都应该改成urllib.request。
'''
import re
from urllib.request import urlopen
from urllib.request import urlretrieve
def getHtml(url):
    page = urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x=0
    for imgurl in imglist:
    	if x<=10:
    		urlretrieve(imgurl,'%s.jpg' % x)
    		x+=1
    	else:pass
    	#没有urllib.urlretrieve的用法了，
    	#现在urlretrieve是在request的方法下面

html = getHtml("http://tieba.baidu.com/p/2460150866")
html = html.decode('utf-8')#没写这句之前，re.findall方法一直报错
'''
page.read()获取的是bytes,而re.findall是查找string里的
改成page.read().encode("utf-8")
'''
print (getImg(html))