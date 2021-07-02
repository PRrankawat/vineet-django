from django.db import models
from django.db.models import Model
# Create your models here.

class MaterialDetail(Model):
    materialID = models.AutoField(primary_key=True)
    material_name = models.CharField(max_length=100, null=True, blank=True)
    material_unit = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'material_detail'