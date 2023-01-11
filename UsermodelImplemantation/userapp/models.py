from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN="ADMIN",'Admin'
        STUDENT="STUDENT",'Student'
        TEACHER="TEACHER",'Teacher'
    #for specific case where by defaut admin
    base_role=Role.ADMIN
    
    role=models.CharField('Role',max_length=50,choices=Role.choices)
    
    def save(self,*args,**kwargs):
        if not self.pk():
            self.role=self.base_role
            return super().save(*args,**kwargs)
    
        
        
        