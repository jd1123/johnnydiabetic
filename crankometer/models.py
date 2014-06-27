from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.


class Crankometer(models.Model):
    was_cranky = models.BooleanField()
    date_verified = models.DateTimeField(auto_now_add=True)
    voter = models.ForeignKey(User, blank=True, null=False)
    votee = models.ForeignKey(User, blank=True, null=False)

class CrankometerAdmin(admin.ModelAdmin):
    list_display = ['date_verified', 'was_cranky']
