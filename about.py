from django.http import request
from django.shortcuts import render  
def ab(request):
    return render(request,"about.html")
