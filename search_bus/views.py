from django.shortcuts import render, redirect
from django.contrib import messages
from .models import details
from django.contrib.auth.models import User , auth

# Create your views here.

def search_bus(request):                                   # render search_bus.html page if user clicks on it on home page
    return render(request, 'search_bus.html')

def search_result(request):                                # search results when user searches for buses
    if request.method == 'POST':                           # Getting details of bus if request is POST
        start_place = request.POST['start_place']          # place from where the bus starts  
        end_place = request.POST['end_place']              # place where bus is destined to
        date = request.POST['date_journey']                # date of the journey
        
        if details.objects.filter(origin_place=start_place , destination_place=end_place , journey_date=date).exists():               # checking if any record exists with specified data
            bus_records = details.objects.filter(origin_place=start_place , destination_place=end_place , journey_date=date)          # creating an object with all the data present in database (if above condition is true) 
            return render(request, 'search_result.html',{'bus_records':bus_records})                                                  # sending all the data to webpage
        else:
            messages.info(request,'NO BUS FOUND')         # print message if no entry is found
            return redirect('search_bus')                 # redirect to the same page
               
    
    else:
        return redirect('search_bus') 

def book_bus(request):                                    # render book_bus.html for booking 
    return render(request,'book_bus.html')

def book_complete(request):                                     # booking bus with data provided by user
    if request.method == 'POST':                                # Getting details of traveller if request is POST
        bus_column = request.POST['column']                     # specify cloumn where passanger wants seat
        bus_row = request.POST['row']                           # specify row where passanger wants seat 
        passenger_first_name = request.POST['first_name']       # passanger's first name
        passenger_last_name = request.POST['last_name']         # passanger's last name
        passenger_age = request.POST['age']                     # passanger's age
        passenger_gender = request.POST['gender']               # passanger's gender
        return render(request,'book_complete.html',{'bus_column':bus_column, 'bus_row':bus_row ,'passenger_first_name':passenger_first_name,
                        'passenger_last_name':passenger_last_name, 'passenger_age':passenger_age, 'passenger_gender':passenger_gender})          # sending all the data from passanger to webpage
    else:
        return redirect('book_bus')