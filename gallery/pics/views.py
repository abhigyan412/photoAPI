from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Photo
from .Serializers import PhotoSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer