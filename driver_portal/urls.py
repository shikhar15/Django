from django.urls import path
from . import views



urlpatterns = [
  
    path('driver_portal', views.driver_portal, name='driver_portal'),
    path('driver_register', views.driver_register, name='driver_register'),
    path('driver_login', views.driver_login, name='driver_login'),
    
]