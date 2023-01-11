from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN="ADMIN",'Admin'
        STUDENT="STUDENT",'Student'
        TEACHER="TEACHER",'Teacher'
    #for specific case where by defaut admin all user to be admin
    base_role=Role.ADMIN
     
    role=models.CharField(max_length=50,choices=Role.choices)
    
    def save(self,*args,**kwargs):
        if not self.pk:
            self.role=self.base_role
            return super().save(*args,**kwargs)
    
class StudentManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results=super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.STUDENT)

class Student(User):
    base_role=User.Role.STUDENT
    student=StudentManager()
    
    class Meta:
        proxy=True
        
    def welcome(self):
        return "Only for students"
    
class TeacherManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results=super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.TEACHER)

class Teacher(User):
    base_role=User.Role.STUDENT
    student=TeacherManager()
    
    class Meta:
        proxy=True
        
    def welcome(self):
        return "Only for Teacher"
    