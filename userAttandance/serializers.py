from .models import UserAttendance
from rest_framework import serializers

class UserAttendanceSerializers(serializers.ModelSerializer):
	class Meta:
		model = UserAttendance
		fields = '__all__'