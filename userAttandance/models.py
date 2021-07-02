from django.db import models
from django.db.models import Model
from django.conf import settings

# Create your models here.

class UserAttendance(Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    site = models.ForeignKey('siteDetails.SiteDetail', on_delete=models.CASCADE)
    attendance = models.CharField(max_length=50, null=True)
    date = models.DateField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    latitude = models.CharField(max_length=50, null=True)
    longitude = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'user_attendance'