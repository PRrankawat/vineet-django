from django.contrib import admin
from .models import StockDetail
# Register your models here.

class StockDetailAdmin(admin.ModelAdmin):
    list_display = ['qty', 'timestamp', 'photo_vehicle', 'photo_material']

admin.site.register(StockDetail, StockDetailAdmin)