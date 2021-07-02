from django.shortcuts import render
from rest_framework import viewsets
from .models import UserAttendance
from .serializers import UserAttendanceSerializers
# Create your views here.

class UserAttendanceAPIViewSet(viewsets.ModelViewSet):
    queryset = UserAttendance.objects.all()
    serializer_class = UserAttendanceSerializers