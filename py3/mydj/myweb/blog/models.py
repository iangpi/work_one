from django.db import models

# Create your models here.
from django.contrib import admin

# 相关数据库表的生成，映射，这里就是数据库，关于数据库的操作都在这里
# 类名——对应数据库里的表名
# 变量——对应数据库里的字段

class Blog(models.Model):
    #Blog集成了models类里的方法，上面第一句导入了models方法
    #在这里创建数据库的表名字（Blog）和变量名字（title，body，timestamp）
    title=models.CharField(max_length=150)#限制标题字数长度
    body=models.TextField()#正文是文本类型
    timestamp=models.DateTimeField()#创建日期显示
