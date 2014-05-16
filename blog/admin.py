from django.contrib import admin
from blog.models import BlogPost, BlogPostAdmin
# Register your models here.

admin.site.register(BlogPost, BlogPostAdmin)
