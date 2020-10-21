from django.shortcuts import render

# Create your views here.
def astar(request):
    return render(request, 'post1.html')

def mindspace(request):
    return render(request, 'post2.html')

def passvault(request):
    return render(request, 'post3.html')
