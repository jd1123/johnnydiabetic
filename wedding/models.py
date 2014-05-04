from django.db import models
from django.contrib import admin

# Create your models here.
class WeddingPic(models.Model):
    pic_name = models.CharField(max_length = 80)
    caption = models.CharField(max_length = 250)
    
    def __unicode__(self):
        return self.pic_name
    
class WeddingPicAdmin(admin.ModelAdmin):
    list_display = ['pic_name', 'caption']
    search_fields = ['pic_name']