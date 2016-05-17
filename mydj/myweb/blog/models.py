from django.db import models
from django.contrib import admin

#create my models
class Blog(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    timestamp=models.DateTimeField()

class BlogAdmin(admin.):