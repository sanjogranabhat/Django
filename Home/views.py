from django.shortcuts import render

# Create your views here.

def index (request):
    
    info ={
        
        'name': "Sanjog",
        'age': 21,
        'location':"pkr"
        
    }
    
    contact={
        'phone':"193713100",
        'email':"sanjog14@gmail.com"
    }
    
    details={
        "information": info,
        "contact": contact,
    }
    
    
    
    return  render(request,'Home/index.html',details)

def about (request):
    
    return  render(request,'Home/about.html')