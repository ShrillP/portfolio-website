from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def astar(request):
    return render(request, 'post1.html')

def mindspace(request):
    return render(request, 'post2.html')

def passvault(request):
    return render(request, 'post3.html')
