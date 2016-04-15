#coding:utf-8
#登录时需要的用户名和密码和提交按钮的元素
login_el={'用户名el':'username',
          '密码el':'password',
          '登录按钮el':'submit'
          }
#登录时要用的用户名和密码
u_p={'用户名':'wxg',
     '密码':'wxg'
     }

'''下面的部分地址，需要完成登陆后才能被使用'''
'''下面的部分地址，需要完成登陆后才能被使用'''
'''下面的部分地址，需要完成登陆后才能被使用'''
url_dict={'登录url':r"http://awsbj-openmanagement.xingyunzhi.cn/developer-user/login",
          '百度测试用url':r"http://www.baidu.com",
          '数据中心url':r"http://awsbj-openmanagement.xingyunzhi.cn/app-bak/get-app-list",
          '编辑密码url':r"http://awsbj-openmanagement.xingyunzhi.cn/account/modify-password?uid=2",
          '用户列表url':r"http://awsbj-openmanagement.xingyunzhi.cn/account/get-user-list",
          '公司列表url':r"http://awsbj-openmanagement.xingyunzhi.cn/account/get-developer-list"}

Datebase_dict={'wxg_el':'html/body/div[1]/div/div/button',
               '修改密码_el':'html/body/div[1]/div/div/ul/li[1]/a',
               '个人信息_el':".//*[@id='modifypasswordpost']/div[1]/h1",
               '搜索按钮_el':".//*[@id='content']/div/div/div/div[2]/div[2]/div/a"
               }