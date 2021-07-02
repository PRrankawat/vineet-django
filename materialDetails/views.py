from django.shortcuts import render
from rest_framework import viewsets
from .models import MaterialDetail
from .serializers import MaterialDetailSerializers
# Create your views here.

class MaterialDetailsAPIViewSet(viewsets.ModelViewSet):
    queryset = MaterialDetail.objects.all()
    serializer_class = MaterialDetailSerializers