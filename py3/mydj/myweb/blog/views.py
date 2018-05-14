from django.shortcuts import render
from blog.models import Blog
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
# 视图文件，作用是承上启下
# 承web页面的下，启数据库的上，起到一个中介作用  web页面《--view--》数据库
# 接收页面请求，请求里带的一些参数。数据库根据前段传来的参数，处理后通过view传递给web页面
def blog(request):
    list_blog=Blog.objects.all()
    for blog in list_blog:
        print (blog.title)
        print (blog.body)
        print (blog.timestamp)
    return render_to_response('blog.html',{'blogs':list_blog})#django里的一个方法，可以用页面形式展示数据。
