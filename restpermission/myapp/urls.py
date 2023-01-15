from django.urls import path
from .views import *

urlpatterns = [
    
    path("", DisasterView.as_view()),   

]
