from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth

# Create your views here.


def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=user_name ,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('register.html')

    else:
        return render(request,'login.html')



def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'Username Already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Registered')
                return redirect('register')
            else:
                user =User.objects.create_user(username=user_name ,password=password1 ,email=email ,first_name=first_name ,last_name =last_name)
                user.save();
                return redirect('login.html')
        else:
            messages.info(request,"password not matching")
            return redirect('register')    
        return redirect('/')

    else:
        return render(request, 'register.html')