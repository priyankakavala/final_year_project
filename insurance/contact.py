from django.http import request
from django.shortcuts import render  
def con(request):
    return render(request,"contact.html")
