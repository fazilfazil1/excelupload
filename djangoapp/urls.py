from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('home/', views.home),
    path('upload_file/', views.upload_file),
    path('read_file/',views.read_file)
]
