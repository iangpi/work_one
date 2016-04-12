#coding:utf-8
import unittest

#login地址
the_real_url=r"http://awsbj-openmanagement.xingyunzhi.cn/developer-user/login"
#测试用的地址
the_baidu_url=r"http://www.baidu.com"
#登录时需要的用户名和密码和提交按钮的元素
el_username='username'
el_password='password'
el_submit='submit'
#登录时要用的用户名和密码
username='wxg'
password='wxg'

'''下面的地址，需要登陆后才能被使用'''

#应用中心地址
app_center_url=r"http://awsbj-openmanagement.xingyunzhi.cn/app-bak/get-app-list"
#修改密码地址
edit_password_url=r"http://awsbj-openmanagement.xingyunzhi.cn/account/modify-password?uid=2"
#帐号列表地址
account_list_url=r"http://awsbj-openmanagement.xingyunzhi.cn/account/get-user-list"
#公司列表地址
company_list_url=r"http://awsbj-openmanagement.xingyunzhi.cn/account/get-developer-list"

if __name__=="__main__":
    unittest.main()