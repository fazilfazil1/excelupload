from django.urls import path
from . import views

# url path setting
urlpatterns = [
    path('',views.index),
    path('customer/', views.customer),
    path('upload_file/', views.upload_file),
    path('read_file/',views.read_file),
    path('product/',views.product),
    path('uploadproduct_file/', views.uploadproduct_file),
    path('order/', views.order),
    path('uploadorder_file/', views.uploadorder_file),
    path('backgroundprocess/', views.backgroundprocess_file),
]
