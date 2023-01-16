from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser 
from DisasterApi.models import *

class User2(AbstractUser):
    
    muni = models.ForeignKey(Municipality,blank=True,on_delete=models.CASCADE,null=True)
    USERNAME_FIELD='username'