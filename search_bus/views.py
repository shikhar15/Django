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
        buscol = request.POST['column']
        busrow = request.POST['row']
        seat = buscol+busrow
        return render(request,'book_complete.html',{'seat':seat})
    else:
        return redirect(book_bus)