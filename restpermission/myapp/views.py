from rest_framework.views import APIView

from rest_framework.generics import GenericAPIView

from rest_framework import permissions,response


from myapp.serializer import *

from myapp.models import *

class DisasterView(APIView):    
         
    def get(self,request):
        disaster=Disaster.objects.all()
        # self.check_object_permissions(request,disaster)
        serializer=DisasterSerializer(disaster,many=True)
        return response.Response(serializer.data)
        
        
        
        

