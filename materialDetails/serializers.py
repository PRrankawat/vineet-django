from rest_framework import serializers
from .models import MaterialDetail

class MaterialDetailSerializers(serializers.ModelSerializer):
	class Meta:
		model = MaterialDetail
		fields = '__all__'