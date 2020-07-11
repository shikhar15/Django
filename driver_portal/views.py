from django.shortcuts import render

# Create your views here.

def driver_portal(request):
    return render(request,'driver_portal.html')


def driver_register(request):
    return render(request,'driver_register.html')


def driver_login(request):
    return render(request,'driver_login.html')
