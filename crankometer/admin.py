from django.contrib import admin
from crankometer.models import Crankometer, CrankometerAdmin
# Register your models here.

admin.site.register(Crankometer, CrankometerAdmin)
