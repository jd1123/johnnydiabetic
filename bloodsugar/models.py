from django.db import models
from django.contrib import admin
# Create your models here.

class BloodSugarEntry(models.Model):
    reading = models.IntegerField()
    entry_time = models.DateTimeField(auto_now_add = True)


class BloodSugarEntryAdmin(admin.ModelAdmin):
    list_display = ['reading', 'entry_time']
    search_fields = ['reading', 'entry_time']
