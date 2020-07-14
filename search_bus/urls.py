from django.urls import path
from . import views



urlpatterns = [
  
    path('search_bus', views.search_bus, name='search_bus'),
    path('search_result', views.search_result, name='search_result'),
    path('book_bus', views.book_bus, name='book_bus'),
    path('book_complete', views.book_complete, name='book_complete'),
]