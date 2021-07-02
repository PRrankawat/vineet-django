from django.contrib import admin
from .models import SiteDetail
# Register your models here.

class SiteDetailAdmin(admin.ModelAdmin):
    list_display = ['siteID', 'site_name']


admin.site.register(SiteDetail, SiteDetailAdmin)