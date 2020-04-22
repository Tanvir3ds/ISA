from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    
    

    return render(request, "index.html",)  

def about(request):
    return render(request, "about.html",)  
    
def contact(request):
    return render(request, "contact.html",)  


# for unknown urls .........................
from django.http import HttpResponse

def error_404_view(request, exception):
    
    return render(request,"error_404.html")


def membership(request):
    return render(request, "membership.html")


def blog(request):
    return render(request, "blog.html")