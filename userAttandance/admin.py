from django.contrib import admin
from .models import UserAttendance
# Register your models here.

class UserAttendanceAdmin(admin.ModelAdmin):
	list_display = ['attendance', 'date', 'time', 'latitude', 'longitude']

admin.site.register(UserAttendance, UserAttendanceAdmin)