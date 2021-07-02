from django.db import models
from django.db.models import Model
from django.conf import settings

# Create your models here.

class StockDetail(Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    site = models.ForeignKey('siteDetails.SiteDetail', on_delete=models.CASCADE)
    material = models.ForeignKey('materialDetails.MaterialDetail', on_delete=models.CASCADE)
    qty = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField()
    photo_vehicle = models.CharField(max_length=255, null=True, blank=True)
    photo_material = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'stock_detail'