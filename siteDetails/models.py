from django.db import models
from django.db.models import Model

# Create your models here.

class SiteDetail(Model):
    siteID = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length=50, null=True, unique=True)

    class Meta:
        db_table = 'site_detail'