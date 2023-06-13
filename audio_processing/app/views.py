from django.shortcuts import render
import os



# Create your views here.
def index(request):
    context = {
    'num_books': 10,
    'num_instances': 10,
    'num_instances_available': 20,
    'num_authors': 90,
    }
    return render(request, 'views/index.html', context=context)
 

def login(request):       
    return render(request, 'views/login.html')

def logout(request):
    request.session.clear()
    return render(request, 'views/login.html')

def register(request):
    return render(request, 'views/register.html')

def documents(request):
    return render(request, 'views/documents.html')

