from django.contrib import admin
from .models import MaterialDetail
# Register your models here.

class MaterialDetailAdmin(admin.ModelAdmin):
	list_display = ['material_name', 'material_unit']

admin.site.register(MaterialDetail, MaterialDetailAdmin)