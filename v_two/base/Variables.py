#coding:utf-8
from selenium import webdriver
#项目地址
the_real_url=r"http://awsbj-openmanagement.xingyunzhi.cn/developer-user/login"
#应用中心地址
app_center_url=r"http://awsbj-openmanagement.xingyunzhi.cn/app-bak/get-app-list"
#测试地址
the_baidu_url=r"http://www.baidu.com"
#浏览器驱动
selenium_driver=webdriver.Firefox()
# chromepath=os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# selenium_driver=webdriver.Chrome(chromepath)
#登录时需要的用户名和密码和提交按钮的元素
el_username='username'
el_password='password'
el_submit='submit'
#登录时要用的用户名和密码
username='wxg'
password='wxg'
