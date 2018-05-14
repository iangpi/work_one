from django.contrib import admin

from blog.models import Blog
# Register your models here.
# 这是django自带后台，用来把数据库里的数据映射到后台。类似公司使用的后台工具。
class BlogAdmin(admin.ModelAdmin):
    list_display=('title','body','timestamp')#list_display的命名是特定格式的

admin.site.register(Blog,BlogAdmin)#从数据库models中，读取数据，显示到admin后台里