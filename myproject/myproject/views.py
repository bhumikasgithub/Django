from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("hello in jango home page of my project")
    return render(request, 'website/index.html') 
def About(request):
    #return HttpResponse("hello in jango about page of my project") 
    return render(request, 'website/about.html')
def contact(request):
    #return HttpResponse("hello in jango project")
    return render(request, 'website/contact.html')