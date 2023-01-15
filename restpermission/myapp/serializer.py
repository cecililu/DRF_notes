from rest_framework import serializers
from myapp.models import *

class MuniSerializer(serializers.ModelSerializer):
    class Meta:    
        model=Muni
        fields= "__all__"
        
class DisasterSerializer(serializers.ModelSerializer):
    Muni=MuniSerializer()
    class Meta:    
        model=Disaster
        fields= "__all__"