from django.shortcuts import render, redirect
from django.contrib import messages
from .models import driver
from search_bus.models import details
from django.contrib.auth.models import auth

# Create your views here.

def driver_portal(request):                                   # render drival portal page if user clicks on it on home page
    return render(request,'driver_portal.html')


def driver_register(request):                        #   -driver registration form operation
    if request.method == 'POST':                     #   Getting details of driver if request is POST
        bus_number = request.POST['bus_no']          #   -number of bus that the driver drives
        first_name = request.POST['first_name']      #   -first name of driver
        last_name = request.POST['last_name']        #   -last name of driver 
        user_name = request.POST['user_name']        #   -username of driver (to be used in driver login)
        email = request.POST['email']                #   -email of driver
        password1 = request.POST['password1']        #   -password (to be used in driver login)
        password2 = request.POST['password2']        #   -password confirmation

        if password1 == password2:                   # -checking if both password matches
            if driver.objects.filter(driver_username=user_name).exists():     # -checking if username is already there in database
                messages.info(request,'Username Already Taken')               # -print message on page if condition is true
                return redirect('driver_register')                            
            elif driver.objects.filter(driver_email=email).exists():    # -checking if email is already used in registration
                messages.info(request,'Email Already Registered')       # -print message on page if condition is true
                return redirect('driver_register')
            elif driver.objects.filter(bus_number=bus_number).exists():    # -checking if bus number is already used in registration
                messages.info(request,'Bus is Already Registered')         # -print message on page if condition is true
                return redirect('driver_register')
            else:                                                    # -creating an object with all data in registration form
                bus_driver =driver.objects.create(driver_username=user_name ,driver_password=password1 ,driver_email=email ,driver_first_name=first_name ,driver_last_name =last_name ,bus_number=bus_number)
                bus_driver.save();                                   # -saveing the object in backend database
                return redirect('driver_login')                      # -redirecting to the login page
        else:
            messages.info(request,"password not matching")           # if password confirmation fails print message on page if condition is true, redirect to same page
            return redirect('driver_register')    
        

    else:
        return render(request, 'driver_register.html')           




def driver_login(request):                                               # driver login page operations
                                                           
    if request.method == 'POST':                                         # getting login details from driver if request is POST
        user_name = request.POST['user_name']                            # username of driver (entered in registration)
        password = request.POST['password']                              # password of driver (entered in registration)

        if driver.objects.filter(driver_username=user_name ,driver_password=password).exists():          # looks for an entry with provided data in specified columns 
            driver_records = driver.objects.filter(driver_username=user_name ,driver_password=password)  # create an object with all data with provided username and password
            for entry in driver_records:                                                                 # looping through every entry in database tuple
                driver_FirstName = entry.driver_first_name                               # storing driver's first name from database(entry.driver_first_name) into a variable(driver_Firstname)
            for record in driver_records:                                         # looping through every entry in database tuple      
                bus_no = record.bus_number                                      # storing bus number from database(record.bus_number) into a variable(bus_no)   
            bus_record = details.objects.filter(bus_number=bus_no)               # create an object with all data with provided bus_number
            return render(request, 'driver_result.html',{'driver_records':driver_records, 
                          'bus_record':bus_record, 'driver_FirstName':driver_FirstName })  #sending all the data to webpage from bus_details and driver details which are in common with bus_number column
            
        else:
            messages.info(request,'Invalid Credentials')      # print message if no entry is found
            return redirect('driver_login')                   # redirect to the same page

    else:
        return render(request,'driver_login.html')          

def logout(request):                      # logout operation
    auth.logout(request)                  # predefined method used to logout
    return redirect('/')                  # redirect to home page
