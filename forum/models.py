from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class Forum(models.Model):
    title = models.CharField(max_length=80)
    
    def __unicode__(self):
        return self.title
    
    def num_posts(self):
        return sum([t.num_posts() for t in self.thread_set.all()])

    def last_post(self):
        if self.thread_set.count():
            last = None
            for t in self.thread_set.all():
                l = t.last_post()
                if l:
                    if not last: last = l
                    elif l.created > last.created: last = l
            return last

class Thread(models.Model):
    forum = models.ForeignKey(Forum)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 120)
    creator = models.ForeignKey(User, blank=True, null=True)
    
    def num_posts(self):
        return self.post_set.count()
    
    def last_post(self):
        if self.post_set.count():
            return self.post_set.order_by("created")[0]
    
    def __unicode__(self):
        return self.title
    
class Post(models.Model):
    thread = models.ForeignKey(Thread)
    created = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length = 120)
    body = models.TextField(max_length = 2000)
    creator = models.ForeignKey(User, blank=True, null=True)
    
    def __unicode__(self):
        return self.subject
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    website=models.URLField(blank=True)
    picture=models.ImageField(upload_to='profile_images', blank=True)
    
    def __unicode__(self):
        return self.user.username

class ForumAdmin(admin.ModelAdmin):
    pass 
    
class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'forum', 'created']
    list_filter = ['forum']
    
class PostAdmin(admin.ModelAdmin):
    list_display = ['subject', 'thread', 'created']
    search_fields = ['subject']