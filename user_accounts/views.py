from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth

# Create your views here.

def login(request):                                          # login operation
    if request.method == 'POST':                             # Getting login details from user if request is POST
        user_name = request.POST['user_name']                # user name of user (entered in registration)
        password = request.POST['password']                  # password of user (entered in registration)

        user = auth.authenticate(username=user_name ,password=password)  # authenticating the username and password

        if user is not None:                          # check if there is a user with provided username and password
            auth.login(request,user)                  # authenticate and login the specified user
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')  # if no user is found, print the message 
            return redirect('login')                      # redirect to same page

    else:
        return render(request,'login.html')



def register(request):                                       # registraion of users

    if request.method == 'POST':                             # Getting details of user if request is POST
        first_name = request.POST['first_name']              # first name of user
        last_name = request.POST['last_name']                # last name of user 
        user_name = request.POST['user_name']                # user name of user (to be used in user login)
        email = request.POST['email']                        # email of user
        password1 = request.POST['password1']                # password of user (to be used in user login) 
        password2 = request.POST['password2']                # password confirmation
    
        if password1 == password2:                                # check for password confirmation
            if User.objects.filter(username=user_name).exists():  # check if username already exists in database
                messages.info(request,'Username Already Taken')   # prints message if condition is true
                return redirect('register')                       # redirect to the same page
            elif User.objects.filter(email=email).exists():               # check if email already exists in database
                messages.info(request,'Email Already Registered')         # prints message if condition is true
                return redirect('register')                                # redirect to the same page
            else:
                user =User.objects.create_user(username=user_name ,password=password1 ,email=email,  # creates a user object with all the details provided by user
                                                 first_name=first_name ,last_name =last_name)
                user.save();                                   # saving the data in backend database
                return redirect('login')                       # redirect to user login page 
        else:
            messages.info(request,"password not matching")     # if password confirmation fails 
            return redirect('register')                        # redirect to same page
        return redirect('/')

    else:
        return render(request, 'register.html')


def logout(request):                      # logout operation
    auth.logout(request)                  # predefined method used to logout
    return redirect('/')                  # redirect to home page

