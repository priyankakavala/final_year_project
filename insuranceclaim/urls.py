from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path("adminhome/",adminhome),
    path("chome/",chome),


    path("agentdetailsform/",agentdetailsform),
    path("agentdetailsview/",agentdetailsview),
    path("useragentdetailsview/",useragentdetailsview),
    path("agentdetailsdelete/<int:agt_id>",agentdetailsdelete),
    path("agentdetailsedit/<int:agt_id>",agentdetailsedit),
    path("agentdetailsupdate/<int:agt_id>",agentdetailsupdate),

    path("claimamountform/",claimamountform),
    path("claimamountformview/",claimamountformview),
    path("claimamountformdelete/<int:camt_id>",claimamountformdelete),
    path("claimamountformedit/<int:camt_id>",claimamountformedit),
    path("claimamountformupdate/<int:camt_id>",claimamountformupdate),


    path("customerdetailsform/",customerdetailsform),
    path("customerdetailsview/",customerdetailsview),
    path("customerdetailsdelete/<int:custd_id>",customerdetailsdelete),
    path("customerdetailsedit/",customerdetailsedit),
    path("customerdetailsupdate/<int:custd_id>",customerdetailsupdate),



    path("customerpolicyform/",customerpolicyform),
    path("customerpolicyview/",customerpolicyview),
    path("usercustomerpolicyview/",usercustomerpolicyview),
    path("customerpolicydelete/<int:cust_id>",customerpolicydelete),
    path("customerpolicyedit/<int:cust_id>",customerpolicyedit),
    path("customerpolicyupdate/<int:cust_id>",customerpolicyupdate),




    path("feedbacktableform/",feedbacktableform),
    path("feedbacktableview/",feedbacktableview),
    path("feedbacktabledelete/<int:fback_id>",feedbacktabledelete),
    path("feedbacktableedit/<int:fback_id>",feedbacktableedit),
    path("feedbacktableupdate/<int:fback_id>",feedbacktableupdate),



    path("insurancecompanydetailsform/",insurancecompanydetailsform),
    path("insurancecompanyview/",insurancecompanyview),
    path("insurancecompanydelete/<int:insu_id>",insurancecompanydelete),
    path("insurancecompanyedit/",insurancecompanyedit),
    path("insurancecompanyupdate/<int:insu_id>",insurancecompanyupdate),


    path("loginform/",loginfor),
    path("loginview/",loginview),
    path("logindelete/<int:log_id>",logindelete),
    path("loginedit/<int:log_id>",loginedit),
    path("loginupdate/<int:log_id>",loginupdate),


    path("policypaymentform/",policypaymentform),
    path("policypaymentview/",policypaymentview),
    path("policypaymentdelete/<int:ppv_id>",policypaymentdelete),
    path("policypaymentedit/<int:ppv_id>",policypaymentedit),
    path("policypaymentupdate/<int:ppv_id>",policypaymentupdate),



    path("policyplandetailsform/",policyplandetailsform),
    path("policyplanview/",policyplanview),
    path("policyplandelete/<int:ppdv_id>",policyplandelete),
    path("policyplanedit/<int:ppdv_id>",policyplanedit),
    path("policyplanupdate/<int:ppdv_id>",policyplanupdate),



    path("vehicleclaimform/",vehicleclaimform),
    path("vehicleclaimview/",vehicleclaimview),
    path("uservehicleclaimview/",uservehicleclaimview),
    path("vehicleclaimdelete/<int:vcv_id>",vehicleclaimdelete),
    path("vehicleclaimedit/<int:vcv_id>",vehicleclaimedit),
    path("vehicleclaimupdate/<int:vcv_id>",vehicleclaimupdate),





   
]
