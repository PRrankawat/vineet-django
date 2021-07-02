from django.shortcuts import render
from rest_framework import viewsets
from .models import StockDetail
from .serializers import StockDetailSerializers
# Create your views here.

class StockDetailsAPIViewSet(viewsets.ModelViewSet):
    queryset = StockDetail.objects.all()
    serializer_class = StockDetailSerializers