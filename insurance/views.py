from django.http import HttpResponse
from django.shortcuts import render,redirect
from insuranceclaim.models import *
from django.contrib import messages




def login(request):
    if request.method=='POST':
        usname=request.POST.get('username')
        passd=request.POST.get('pass')
        #user=authenticate(request,username=usname,password=passd)
        user_count = customer_details.objects.filter(customer_firstname=usname,mobile_no=passd).count()
        if user_count > 0:
            #login (request,user)
            user=customer_details.objects.filter(customer_firstname=usname,mobile_no=passd).first()
            request.session['usersession']=True
            request.session['userid']=usname
            request.session['u_id']=user.id
            return redirect("/insuranceclaim/adminhome/")
        else:
            return HttpResponse('Invalid Username And Password!!! ')   
    return render(request,"login.html")
   
def clogin(request):
    if request.method=='POST':
        usname=request.POST.get('username')
        passd=request.POST.get('pass')
        #user=authenticate(request,username=usname,password=passd)
        c_count = insurance_company_details.objects.filter(insurance_name=usname,insurance_contact_no=passd).count()
        if  c_count > 0:
            #login (request,user)
            c_count = insurance_company_details.objects.filter(insurance_name=usname,insurance_contact_no=passd).first()
            request.session['csession']=True
            request.session['cid']=usname
            request.session['c_id']=c_count.id
            return redirect("/insuranceclaim/chome/")
        else:
            return HttpResponse('Invalid Username And Password!!! ')   
    return render(request,"clogin.html")

def register(request):
    try:
        if request.method=="POST":
            uname=request.POST.get("username")
            password=request.POST.get("password")
            usertype=request.POST.get("usertype")
            hintq=request.POST.get("hintq")
            hinta=request.POST.get("hinta")


            a=loginform()
            a.username=uname
            a.password=password
            a.usertype=usertype
            a.hintq=hintq
            a.hinta=hinta
            a.save()    
    except Exception as e:
          print(e)
          messages.success(request,"Registered sucessfully...")
          return redirect("/login/")
    return render(request,"register.html")
  

def home(request):
    return render(request,"home.html")


def changepin(request):  
     return render(request,"adminhome/changepin.html")

def changepin_chk(request):   
     if request.method=="POST":
        uid=request.session['userid']
        op=request.POST.get("op")
        np=request.POST.get("np")
        cp=request.POST.get("cp")
        if loginform.objects.filter(username=uid,password=op) and np==cp: 
          u=loginform.objects.get(username=uid)
          print(op)
          print(np)
          print(cp)
          print(uid)
          u.password=np
          u.save()
          messages.success(request,"password changed sucessfully...")     
        else:
          messages.success(request,"Unmatched old password...")     
     return render(request,"adminhome/changepin.html")



def LogoutPage(request):
    del request.session['usersession']
    return redirect('/')
def cLogoutPage(request):
    del request.session['csession']
    return redirect('/')


