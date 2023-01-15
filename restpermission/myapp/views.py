from rest_framework.views import APIView

from rest_framework.generics import ListAPIView,RetrieveAPIView

from rest_framework import permissions,response
from rest_framework.decorators import permission_classes


from myapp.serializer import *

from myapp.models import *
from django.shortcuts import get_object_or_404



class Disasterview1(APIView):
    @permission_classes([permissions.IsAuthenticated])
    def get(self,request,pk):
        disaster=Disaster.objects.get(id=pk)
        serializer=DisasterSerializer(disaster)
        return response.Response(serializer.data)
         
class DisasterView(ListAPIView): 
    serializer_class=DisasterSerializer      
    queryset=Disaster.objects.all()
    
    # @permission_classes([permissions.AllowAny])
    # def get(self,request):
    #     disaster=Disaster.objects.all()
    #     serializer=DisasterSerializer(disaster,many=True)
    #     return response.Response(serializer.data)
   
    # @permission_classes([permissions.IsAuthenticated])
    # def patch(self,request,pk): 
    #     data=Disaster.object.get(id=pk)
    #     serializer=DisasterSerializer(data,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response('ok done') 
            
            
            
class DisasterViewDetail(RetrieveAPIView): 
    serializer_class=DisasterSerializer      
    permission_classes=[permissions.IsAuthenticated]
    
    # queryset=Disaster.objects.get(id=pk)
    
    def get(self,request,pk):
        disaster=Disaster.objects.get(id=pk)
        serializer=DisasterSerializer(disaster)
        return response.Response(serializer.data)
    
    def patch(self,request,pk):    
        data=Disaster.objects.get(id=pk)
        serializer=DisasterSerializer(data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response('ok done') 

from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.permissions import DjangoObjectPermissions

from .models import Disaster
from myapp.serializer import DisasterSerializer          

class DisasterObj(viewsets.ModelViewSet):
    permission_classes = [DjangoObjectPermissions,permissions.IsAuthenticated] 
    queryset = Disaster.objects.all()
    serializer_class = DisasterSerializer

    # def perform_create(self, serializer): # new function
    #     instance = serializer.save()
    #     assign_perm("myapp.delete_disaster", self.request.user, instance)
    
                 
            
            
        
        
