from django.shortcuts import render
from rest_framework import viewsets
from .models import SiteDetail
from .serializers import SiteDetailSerializers
# Create your views here.

class SiteDetailsAPIViewSet(viewsets.ModelViewSet):
    queryset = SiteDetail.objects.all()
    serializer_class = SiteDetailSerializers