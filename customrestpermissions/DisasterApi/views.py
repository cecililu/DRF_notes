from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .permissions import AuthorAllStaffAllButEditOrReadOnly
from .models import *
from rest_framework import serializers
# from rest_framework import permissions


class MainSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Main
        fields="__all__"      
         
class ViewTest(ModelViewSet):
      permission_classes=[AuthorAllStaffAllButEditOrReadOnly]
      queryset= Main.objects.all()   
      serializer_class=MainSerializer    