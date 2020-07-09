from django.shortcuts import render
from .models import details
# Create your views here.

def search_bus(request):

    return render(request, 'search_bus.html')

def search_result(request):

    bus_records = details.objects.filter(origin_place='Jaipur')
    return render(request, 'search_result.html',{'bus_records':bus_records})