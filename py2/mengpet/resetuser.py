from selenium import webdriver
from time import sleep
import os
user_info=open('./input_your_url.txt','r')
a=user_info.readline()
print a
str(a)
#user_url=('http://pets.xingyunzhi.cn:3000/index.html?inviter=e55bcbd9525a721633671935007f359e&v=0.0.105&source=2&firstLogin=1')
user_id=a[65:97]
base_url='http://pets.xingyunzhi.cn:3000/users/tweak?action=remove_user&id='
the_url=base_url+user_id
print the_url
print ('your id number is : %s')% user_id
#ff=webdriver.Firefox()
phantomjs_path=os.path.abspath(r"C:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe")
ff=webdriver.PhantomJS(phantomjs_path)
ff.get(the_url)
print ('had reset your account')
sleep(2)
ff.close()