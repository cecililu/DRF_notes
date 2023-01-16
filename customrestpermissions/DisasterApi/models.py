from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Municipality(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
   
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser

class Main(models.Model):
    name=models.CharField(max_length=200)
    muni=models.ForeignKey(Municipality,on_delete=models.CASCADE,blank=True,null=True)
     
# class User(AbstractUser):
#     muni = models.ForeignKey(Municipality,blank=True,on_delete=models.CASCADE,null=True)
#     USERNAME_FIELD='username'