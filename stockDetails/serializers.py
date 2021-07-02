from .models import StockDetail
from rest_framework import serializers

class StockDetailSerializers(serializers.ModelSerializer):
	class Meta:
		model = StockDetail
		fields = '__all__'