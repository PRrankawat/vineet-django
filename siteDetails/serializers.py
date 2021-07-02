from .models import SiteDetail
from rest_framework import serializers

class SiteDetailSerializers(serializers.ModelSerializer):
	class Meta:
		model = SiteDetail
		fields = '__all__'