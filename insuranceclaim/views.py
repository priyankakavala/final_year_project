from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
def adminhome(request):
    return render(request,"adminhome/home.html")
# Create your views here.
def chome(request):
    return render(request,"adminhome/chome.html")

def agentdetailsform(request):
    if request.method=="POST":
        cmid=request.POST.get("company_id")
        fcmid=insurance_company_details.objects.get(id=cmid)

        agntname=request.POST.get("agent_name")
        dob=request.POST.get("dob")
        gen=request.POST.get("gender")
        adrs=request.POST.get("address")
        city=request.POST.get("city")
        cono=request.POST.get("contact_no")
        e_mail=request.POST.get("email")
        

        a=agent_details()
        a.company_id=fcmid
        a.agent_name=agntname
        a.dob=dob
        a.gender=gen
        a.address=adrs
        a.city=city
        a.contact_no=cono
        a.email=e_mail
        a.save()
        return redirect("/insuranceclaim/agentdetailsview/")
    return render(request,"adminhome/agentdetailsform.html",{'cust':insurance_company_details.objects.all()})


def agentdetailsview(request):
    c_id=request.session['c_id']
    agnt=agent_details.objects.filter(company_id=c_id)
    return render(request,'adminhome/agentdetailsview.html',{'agnt':agnt})

def useragentdetailsview(request):
    #c_id=request.session['c_id']
    agnt=agent_details.objects.all()
    return render(request,'adminhome/useragentdetailsview.html',{'agnt':agnt})

def agentdetailsdelete(request,agt_id):
    agnt=agent_details.objects.get(id=agt_id)
    agnt.delete()
    return redirect("/insuranceclaim/agentdetailsview/")

def agentdetailsedit(request,agt_id):
    agnt=agent_details.objects.get(id=agt_id)
    return render(request,"adminhome/agentdetailsedit.html",{'agnt':agnt,'cust':insurance_company_details.objects.all()})

def agentdetailsupdate(request,agt_id):
    if request.method=="POST":
        cmid=request.POST.get("company_id")
        fcmid=insurance_company_details.objects.get(id=cmid)

        agntname=request.POST.get("agent_name")
        dob=request.POST.get("dob")
        gen=request.POST.get("gender")
        adrs=request.POST.get("address")
        city=request.POST.get("city")
        cono=request.POST.get("contact_no")
        e_mail=request.POST.get("email")

        a=agent_details(id=agt_id)
        a.company_id=fcmid
        a.agent_name=agntname
        a.dob=dob
        a.gender=gen
        a.address=adrs
        a.city=city
        a.contact_no=cono
        a.email=e_mail
        a.save()
        return redirect("/insuranceclaim/agentdetailsview/")

def claimamountform(request):
    if request.method=="POST":
        custid=request.POST.get("customer_policy_id")
        fcustid=customer_policy.objects.get(id=custid)

        total=request.POST.get("total_valuation")
        redate=request.POST.get("release_date")
        relamt=request.POST.get("release_amount")
        
        a=claim_amount()
        a.customer_policy_id=fcustid
        a.total_valuation=total
        a.release_date=redate
        a.release_amount=relamt
        a.save()
        return redirect("/insuranceclaim/claimamountformview/")
    return render(request,"adminhome/claimamountform.html",{'cust':customer_policy.objects.all()})

def claimamountformview(request):
    camt=claim_amount.objects.all()
    return render(request,'adminhome/claimamountformview.html',{'camt':camt})

def claimamountformdelete(request,camt_id):
    camt=claim_amount.objects.get(id=camt_id)
    camt.delete()
    return redirect("/insuranceclaim/claimamountformview/")

def claimamountformedit(request,camt_id):
    camt=claim_amount.objects.get(id=camt_id)
    return render(request,'adminhome/claimamountformedit.html',{'camt':camt,'cust':customer_policy.objects.all()})

def claimamountformupdate(request,camt_id):
    if request.method=="POST":
        custid=request.POST.get("customer_policy_id")
        fcustid=customer_policy.objects.get(id=custid)

        total=request.POST.get("total_valuation")
        redate=request.POST.get("release_date")
        relamt=request.POST.get("release_amount")
        
        a=claim_amount(id=camt_id)
        a.customer_policy_id=fcustid
        a.total_valuation=total
        a.release_date=redate
        a.release_amount=relamt
        a.save()
        return redirect("/insuranceclaim/claimamountformview/")

def customerdetailsform(request):
    if request.method=="POST":
        custfname=request.POST.get("customer_firstname")
        custlname=request.POST.get("customer_lastname")
        dob=request.POST.get("dob")
        gen=request.POST.get("gender")
        adrs=request.POST.get("address")
        city=request.POST.get("city")
        mno=request.POST.get("mobile_no")
        e_mail=request.POST.get("email_id")
        image=request.FILES.get("image")

        
        a=customer_details()
        a.customer_firstname=custfname
        a.customer_lastname=custlname
        a.dob=dob
        a.gender=gen
        a.address=adrs
        a.city=city
        a.mobile_no=mno
        a.email_id=e_mail
        a.image=image
        a.save()
        return redirect("/insuranceclaim/customerdetailsview/")

    return render(request,"adminhome/customerdetailsform.html")

def customerdetailsview(request):
    custd=customer_details.objects.all()
    return render(request,'adminhome/customerdetailsview.html',{'custd':custd})

def customerdetailsdelete(request,custd_id):
    custd=customer_details.objects.get(id=custd_id)
    custd.delete()
    return redirect("/insuranceclaim/customerdetailsview/")

def customerdetailsedit(request):
    custd_id=request.session['u_id']
    custd=customer_details.objects.filter(id=custd_id)
    return render(request,'adminhome/customerdetailsedit.html',{'custd':custd})

def customerdetailsupdate(request,custd_id):
    if request.method=="POST":
        custfname=request.POST.get("customer_firstname")
        custlname=request.POST.get("customer_lastname")
        dob=request.POST.get("dob")
        gen=request.POST.get("gender")
        adrs=request.POST.get("address")
        city=request.POST.get("city")
        mno=request.POST.get("mobile_no")
        e_mail=request.POST.get("email_id")
        image=request.POST.get("image")

        
        a=customer_details(id=custd_id)
        a.customer_firstname=custfname
        a.customer_lastname=custlname
        a.dob=dob
        a.gender=gen
        a.address=adrs
        a.city=city
        a.mobile_no=mno
        a.email_id=e_mail
        a.image=image
        a.save()
        return redirect("/insuranceclaim/customerdetailsview/")


def customerpolicyform(request):
    if request.method=="POST":
        custid=request.POST.get("customer_id")
        fcustid=customer_details.objects.get(id=custid)

        agnid=request.POST.get("agent_id")
        fagnid=agent_details.objects.get(id=agnid)

        poid=request.POST.get("policy_plan_id")
        fpoid=policy_plan_details.objects.get(id=poid)


        tamount=request.POST.get("total_amount")
        iamount=request.POST.get("installment_amount")
        psdate=request.POST.get("policy_start_date")
        pedate=request.POST.get("policy_end_date")
        
        a=customer_policy()
        a.customer_id=fcustid
        a.agent_id=fagnid
        a.policy_plan_id=fpoid
        a.total_amount=tamount
        a.installment_amount=iamount
        a.policy_start_date=psdate
        a.policy_end_date=pedate
        a.save()
        return redirect("/insuranceclaim/customerpolicyview/")
    return render(request,"adminhome/customerpolicyform.html",{'cust':customer_details.objects.all(),'cust1':agent_details.objects.all(),'cust2':policy_plan_details.objects.all()})

def customerpolicyview(request):
    cust=customer_policy.objects.all()
    return render(request,'adminhome/customerpolicyview.html',{'cust':cust})

def usercustomerpolicyview(request):
    uid=request.session['u_id']
    cust=customer_policy.objects.filter(id=uid)
    return render(request,'adminhome/usercustomerpolicyview.html',{'cust':cust})

def customerpolicydelete(request,cust_id):
    cust=customer_policy.objects.get(id=cust_id)
    cust.delete()
    return redirect("/insuranceclaim/customerpolicyview/")

def customerpolicyedit(request,cust_id):
    cuest=customer_policy.objects.get(id=cust_id)
    return render(request,'adminhome/customerpolicyedit.html',{'cuest':cuest,'cust':customer_details.objects.all(),'cust1':agent_details.objects.all(),'cust2':policy_plan_details.objects.all()})

def customerpolicyupdate(request,cust_id):
    if request.method=="POST":
        custid=request.POST.get("customer_id")
        fcustid=customer_details.objects.get(id=custid)

        agnid=request.POST.get("agent_id")
        fagnid=agent_details.objects.get(id=agnid)

        poid=request.POST.get("policy_plan_id")
        fpoid=policy_plan_details.objects.get(id=poid)


        tamount=request.POST.get("total_amount")
        iamount=request.POST.get("installment_amount")
        psdate=request.POST.get("policy_start_date")
        pedate=request.POST.get("policy_end_date")
        
        a=customer_policy(id=cust_id)
        a.customer_id=fcustid
        a.agent_id=fagnid
        a.policy_plan_id=fpoid
        a.total_amount=tamount
        a.installment_amount=iamount
        a.policy_start_date=psdate
        a.policy_end_date=pedate
        a.save()
        return redirect("/insuranceclaim/customerpolicyview/")


def feedbacktableform(request):
    if request.method=="POST":
        to=request.POST.get("to")
        title=request.POST.get("title")
        feedback_msg=request.POST.get("feedback_msg")
        date=request.POST.get("date")

        a=feedback_table()
        a.to=to
        a.title=title
        a.feedback_msg=feedback_msg
        a.date=date
        a.save()
        return redirect("/insuranceclaim/feedbacktableview/")
    return render(request,"adminhome/feedbacktableform.html")

def feedbacktableview(request):
    fback=feedback_table.objects.all()
    return render(request,'adminhome/feedbacktableview.html',{'fback':fback})

def feedbacktabledelete(request,fback_id):
    fback=feedback_table.objects.get(id=fback_id)
    fback.delete()
    return redirect("/insuranceclaim/feedbacktableview/")

def feedbacktableedit(request,fback_id):
    fback=feedback_table.objects.get(id=fback_id)
    return render(request,'adminhome/feedbacktableedit.html',{'fback':fback})

def feedbacktableupdate(request,fback_id):
    if request.method=="POST":
        to=request.POST.get("to")
        title=request.POST.get("title")
        feedback_msg=request.POST.get("feedback_msg")
        date=request.POST.get("date")

        a=feedback_table(id=fback_id)
        a.to=to
        a.title=title
        a.feedback_msg=feedback_msg
        a.date=date
        a.save()
        return redirect("/insuranceclaim/feedbacktableview/")

def insurancecompanydetailsform(request):
    if request.method=="POST":
        iname=request.POST.get("insurance_name")
        iaddress=request.POST.get("insurance_address")
        icity=request.POST.get("insurance_city")
        icontact=request.POST.get("insurance_contact_no")
        website=request.POST.get("website")
        email_id=request.POST.get("email_id")
        
        
        a=insurance_company_details()
        a.insurance_name=iname
        a.insurance_address=iaddress
        a.insurance_city=icity
        a.insurance_contact_no=icontact
        a.website=website
        a.email_id=email_id
        a.save()
        return redirect("/insuranceclaim/insurancecompanyview/")

    return render(request,"adminhome/insurancecompanydetailsform.html")

def insurancecompanyview(request):
    insu=insurance_company_details.objects.all()
    return render(request,'adminhome/insurancecompanyview.html',{'insu':insu})

def insurancecompanydelete(request,insu_id):
    insu=insurance_company_details.objects.get(id=insu_id)
    insu.delete()
    return redirect("/insuranceclaim/insurancecompanyview/")

def insurancecompanyedit(request):
    c_id=request.session['c_id']
    #print(c_id)
    comp_id=insurance_company_details.objects.filter(id=c_id)
    return render(request,'adminhome/insurancecompanyedit.html',{'insu':comp_id})

def insurancecompanyupdate(request,insu_id):
     if request.method=="POST":
        iname=request.POST.get("insurance_name")
        iaddress=request.POST.get("insurance_address")
        icity=request.POST.get("insurance_city")
        icontact=request.POST.get("insurance_contact_no")
        website=request.POST.get("website")
        email_id=request.POST.get("email_id")
        
        
        a=insurance_company_details(id=insu_id)
        a.insurance_name=iname
        a.insurance_address=iaddress
        a.insurance_city=icity
        a.insurance_contact_no=icontact
        a.website=website
        a.email_id=email_id
        a.save()
        return redirect("/insuranceclaim/insurancecompanyview/")


def loginfor(request):
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
        return redirect("/insuranceclaim/loginview/")
    return render(request,"adminhome/loginform.html")

def loginview(request):
    log=loginform.objects.all()
    return render(request,'adminhome/loginview.html',{'log':log})

def logindelete(request,log_id):
    log=loginform.objects.get(id=log_id)
    log.delete()
    return redirect("/insuranceclaim/loginview/")

def loginedit(request,log_id):
    log=loginform.objects.get(id=log_id)
    return render(request,'adminhome/loginedit.html',{'log':log})

def loginupdate(request,log_id):
    if request.method=="POST":
        uname=request.POST.get("username")
        password=request.POST.get("password")
        usertype=request.POST.get("usertype")
        hintq=request.POST.get("hintq")
        hinta=request.POST.get("hinta")

        a=loginform(id=log_id)
        a.username=uname
        a.password=password
        a.usertype=usertype
        a.hintq=hintq
        a.hinta=hinta
        a.save()
        return redirect("/insuranceclaim/loginview/")

def policypaymentform(request):
    if request.method=="POST":
        custpid=request.POST.get("customer_policy_id")
        fcustpid=customer_policy.objects.get(id=custpid)

        pamount=request.POST.get("paid_amount")
        pdata=request.POST.get("paid_data")
        

        a=policy_payments()
        a.customer_policy_id=fcustpid
        a.paid_amount=pamount
        a.paid_data=pdata
        a.save()
        return redirect("/insuranceclaim/policypaymentview/")   
    return render(request,"adminhome/policypaymentform.html",{'cust':customer_policy.objects.all()})

def policypaymentview(request):
    ppv=policy_payments.objects.all()
    return render(request,'adminhome/policypaymentview.html',{'ppv':ppv})

def policypaymentdelete(request,ppv_id):
    ppv=policy_payments.objects.get(id=ppv_id)
    ppv.delete()
    return redirect("/insuranceclaim/policypaymentview/")

def policypaymentedit(request,ppv_id):
    ppv=policy_payments.objects.get(id=ppv_id)
    return render(request,'adminhome/policypaymentedit.html',{'ppv':ppv,'cust':customer_policy.objects.all()})

def policypaymentupdate(request,ppv_id):
    if request.method=="POST":
        custpid=request.POST.get("customer_policy_id")
        fcustpid=customer_policy.objects.get(id=custpid)

        pamount=request.POST.get("paid_amount")
        pdata=request.POST.get("paid_data")
        

        a=policy_payments(id=ppv_id)
        a.customer_policy_id=fcustpid
        a.paid_amount=pamount
        a.paid_data=pdata
        a.save()
        return redirect("/insuranceclaim/policypaymentview/")   

def policyplandetailsform(request):
    if request.method=="POST":
        pnumber=request.POST.get("policy_number")
        pname=request.POST.get("policy_name")
        duration=request.POST.get("duration")
        pdetails=request.POST.get("policy_details")
        cid=request.POST.get("cid")
        c_id=insurance_company_details.objects.get(id=cid)
        

        a=policy_plan_details()
        a.policy_number=pnumber
        a.policy_name=pname
        a.duration=duration
        a.policy_details=pdetails
        a.company_id=c_id
        a.save()
        return redirect("/insuranceclaim/policyplanview/")
    return render(request,"adminhome/policyplandetailsform.html")

def policyplanview(request):
    c_id=request.session['c_id']
    ppdv=policy_plan_details.objects.filter(company_id=c_id)
    return render(request,'adminhome/policyplanview.html',{'ppdv':ppdv})

def policyplandelete(request,ppdv_id):
    ppdv=policy_plan_details.objects.get(id=ppdv_id)
    ppdv.delete()
    return redirect("/insuranceclaim/policyplanview/")

def policyplanedit(request,ppdv_id):
    ppdv=policy_plan_details.objects.get(id=ppdv_id)
    return render(request,'adminhome/policyplanedit.html',{'ppdv':ppdv})

def policyplanupdate(request,ppdv_id):
    if request.method=="POST":
        pnumber=request.POST.get("policy_number")
        pname=request.POST.get("policy_name")
        duration=request.POST.get("duration")
        pdetails=request.POST.get("policy_details")
        

        a=policy_plan_details(id=ppdv_id)
        a.policy_number=pnumber
        a.policy_name=pname
        a.duration=duration
        a.policy_details=pdetails
        a.save()
        return redirect("/insuranceclaim/policyplanview/")

def vehicleclaimform(request):
    uid=request.GET.get('id')
    if request.method=="POST":
        custid=request.POST.get("customer_id")
        fcid=customer_details.objects.get(id=custid)

        custpid=request.POST.get("customer_policy_id")
        fcustpid=customer_policy.objects.get(id=custpid)

        ctype=request.POST.get("claim_type")
        vnumber=request.POST.get("vehicle_number")
        vname=request.POST.get("vehicle_name")
        vvalue=request.POST.get("vehicle_value")
        vcondition=request.POST.get("vehicle_condition")
        image_1=request.FILES.get("image_1")
        image_2=request.FILES.get("image_2")
        image_3=request.FILES.get("image_3")
        status=request.POST.get("status")

        
        a=vehicle_claim()
        a.customer_id=fcid
        a.customer_policy_id=fcustpid
        a.claim_type=ctype
        a.vehicle_number=vnumber
        a.vehicle_name=vname
        a.vehicle_value=vvalue
        a.vehicle_condition=vcondition
        a.image_1=image_1
        a.image_2=image_2
        a.image_3=image_3
        a.status=status
        a.save()
        return redirect("/insuranceclaim/uservehicleclaimview/")

    return render(request,"adminhome/vehicleclaimform.html",{'cust':customer_policy.objects.filter(id=uid),'custplyc':customer_policy.objects.all()})

def vehicleclaimview(request):
    vcv=vehicle_claim.objects.all()
    return render(request,'adminhome/vehicleclaimview.html',{'vcv':vcv})

def uservehicleclaimview(request):
    vcv=vehicle_claim.objects.all()
    return render(request,'adminhome/uservehicleclaimview.html',{'vcv':vcv})

def vehicleclaimdelete(request,vcv_id):
    vcv=vehicle_claim.objects.get(id=vcv_id)
    vcv.delete()
    return redirect("/insuranceclaim/vehicleclaimview/")

def vehicleclaimedit(request,vcv_id):
    vcv=vehicle_claim.objects.get(id=vcv_id)
    return render(request,'adminhome/vehicleclaimedit.html',{'vcv':vcv,'cust':customer_details.objects.all(),'custplyc':customer_policy.objects.all()})

def vehicleclaimupdate(request,vcv_id):
    if request.method=="POST":
        custid=request.POST.get("customer_id")
        fcid=customer_details.objects.get(id=custid)

        custpid=request.POST.get("customer_policy_id")
        fcustpid=customer_policy.objects.get(id=custpid)

        ctype=request.POST.get("claim_type")
        vnumber=request.POST.get("vehicle_number")
        vname=request.POST.get("vehicle_name")
        vvalue=request.POST.get("vehicle_value")
        vcondition=request.POST.get("vehicle_condition")
        image_1=request.POST.get("image_1")
        image_2=request.POST.get("image_2")
        image_3=request.POST.get("image_3")
        status=request.POST.get("status")

        
        a=vehicle_claim(id=vcv_id)
        a.customer_id=fcid
        a.customer_policy_id=fcustpid
        a.claim_type=ctype
        a.vehicle_number=vnumber
        a.vehicle_name=vname
        a.vehicle_value=vvalue
        a.vehicle_condition=vcondition
        a.image_1=image_1
        a.image_2=image_2
        a.image_3=image_3
        a.status=status
        a.save()
        return redirect("/insuranceclaim/vehicleclaimview/")
