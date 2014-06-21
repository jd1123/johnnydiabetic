from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    search_fields = ['title', 'created']
