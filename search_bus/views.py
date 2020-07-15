from django.shortcuts import render, redirect
from django.contrib import messages
from .models import details
from django.contrib.auth.models import User , auth

# Create your views here.

def search_bus(request):

    return render(request, 'search_bus.html')

def search_result(request):
    if request.method == 'POST':
        start_place = request.POST['start_place']
        end_place = request.POST['end_place']
        date = request.POST['date_journey']
        
        if details.objects.filter(origin_place=start_place , destination_place=end_place , journey_date=date).exists():
            bus_records = details.objects.filter(origin_place=start_place , destination_place=end_place , journey_date=date)
            return render(request, 'search_result.html',{'bus_records':bus_records})
        else:
            messages.info(request,'NO BUS FOUND')
            return redirect('search_bus')
               
    
    else:
        return redirect('search_bus') 

def book_bus(request):
    return render(request,'book_bus.html')

def book_complete(request):
    if request.method == 'POST':
        bus_column = request.POST['column']
        bus_row = request.POST['row']
        passenger_first_name = request.POST['first_name']
        passenger_last_name = request.POST['last_name']
        passenger_age = request.POST['age']
        passenger_gender = request.POST['gender']
        return render(request,'book_complete.html',{'bus_column':bus_column, 'bus_row':bus_row ,'passenger_first_name':passenger_first_name,
                        'passenger_last_name':passenger_last_name, 'passenger_age':passenger_age, 'passenger_gender':passenger_gender})
    else:
        return redirect('book_bus')