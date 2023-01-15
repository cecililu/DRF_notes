from django.urls import path
from .views import *

urlpatterns = [
    
    path("test", DisasterView.as_view()),
    path("test1/<int:pk>", DisasterViewDetail.as_view())   

]
