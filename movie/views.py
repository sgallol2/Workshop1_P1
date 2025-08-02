from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return render(request, 'home.html')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name': 'Sofia Gallo la Rosa'})

def about(request):
    return HttpResponse('<h1>About Us</h1>')