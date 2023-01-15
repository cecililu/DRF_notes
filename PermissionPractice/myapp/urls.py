from django.contrib import admin
from django.urls import path,include
from myapp.views import *

urlpatterns = [
    path("", PostListView.as_view()),
    path("model", PostListViewModelLevel.as_view()),
]