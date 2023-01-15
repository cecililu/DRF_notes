from django.db import models

# Create your models here.

class Muni(models.Model):
    name=models.CharField(max_length=100)        

class Disaster(models.Model):
    name=models.CharField(max_length=100) 
    Muni=models.ForeignKey(Muni,on_delete=models.CASCADE)
       