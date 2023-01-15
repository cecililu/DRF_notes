from django.urls import path,include
from .views import *
from rest_framework import routers
rouet=routers.DefaultRouter()

rouet.register('',DisasterObj)

urlpatterns = [
    
    path("test", DisasterView.as_view()),
    path("test1/<int:pk>", DisasterViewDetail.as_view()) ,
    #writing Apiview instasted of GEneric to see if decorator can be used
    #connecyed wth DisasaterView1
    path("test2/<int:pk>", DisasterViewDetail.as_view()), 
     #ok this works
    path('obj/',include(rouet.urls))
]
