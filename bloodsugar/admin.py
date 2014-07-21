from django.contrib import admin
from bloodsugar.models import BloodSugarEntry, BloodSugarEntryAdmin
# Register your models here.

admin.site.register(BloodSugarEntry, BloodSugarEntryAdmin)
