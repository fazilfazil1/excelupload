from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('upload_file/', views.upload_file)
]
