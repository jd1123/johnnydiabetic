from django.contrib import admin
from forum.models import Forum, ForumAdmin, Thread, ThreadAdmin, Post, PostAdmin, UserProfile

# Register your models here.

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)