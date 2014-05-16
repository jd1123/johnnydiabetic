from django.db import models
from django.contrib import admin

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    search_fields = ['title', 'created']