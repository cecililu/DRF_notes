from rest_framework.views import APIView

from rest_framework.generics import ListAPIView,RetrieveAPIView

from rest_framework import permissions,response
from rest_framework.decorators import permission_classes


from myapp.serializer import *

from myapp.models import *
from django.shortcuts import get_object_or_404

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
    
    @permission_classes([permissions.AllowAny])
    def get(self,request,pk):
        disaster=Disaster.objects.get(id=pk)
        serializer=DisasterSerializer(disaster)
        return response.Response(serializer.data)
   
    @permission_classes([permissions.IsAuthenticated])
    def patch(self,request,pk): 
        data=Disaster.objects.get(id=pk)
        serializer=DisasterSerializer(data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response('ok done') 

            
            
                 
            
            
        
        
