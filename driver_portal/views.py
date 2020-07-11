from django.shortcuts import render, redirect
from django.contrib import messages
from .models import driver
from search_bus.models import details
from django.contrib.auth.models import auth

# Create your views here.

def driver_portal(request):
    return render(request,'driver_portal.html')


def driver_register(request):   
    if request.method == 'POST':
        bus_number = request.POST['bus_no']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if driver.objects.filter(driver_username=user_name).exists():
                messages.info(request,'Username Already Taken')
                return redirect('driver_register')
            elif driver.objects.filter(driver_email=email).exists():
                messages.info(request,'Email Already Registered')
                return redirect('driver_register')
            else:
                bus_driver =driver.objects.create(driver_username=user_name ,driver_password=password1 ,driver_email=email ,driver_first_name=first_name ,driver_last_name =last_name ,bus_number=bus_number)
                bus_driver.save();
                return redirect('driver_login')
        else:
            messages.info(request,"password not matching")
            return redirect('driver_register')    
        

    else:
        return render(request, 'driver_register.html')




def driver_login(request):
    bus_no = ""
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']

        if driver.objects.filter(driver_username=user_name ,driver_password=password).exists():
            driver_records = driver.objects.filter(driver_username=user_name ,driver_password=password)
            for record in driver_records:
                bus_no = record.bus_number
            bus_record = details.objects.filter(bus_number=bus_no)
            return render(request, 'driver_result.html',{'driver_records':driver_records, 'bus_record':bus_record })
            
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('driver_login')

    else:
        return render(request,'driver_login.html')

