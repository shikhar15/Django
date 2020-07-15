from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):                                       # render home page 
    return render(request, 'home.html')

