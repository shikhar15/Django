from django.urls import path
from . import views


urlpatterns = [
  
    path('search_bus', views.search_bus, name='search_bus'),
    path('search_result', views.search_result, name='search_result')
]