from django.contrib import admin
from .models import *
# Register your models here.
class customer(admin.ModelAdmin):
    list_display=('id','customer_firstname','customer_lastname','dob','gender','address','city','mobile_no','email_id','image')
admin.site.register(customer_details,customer)

class policy_plan(admin.ModelAdmin):
    list_display=('id','policy_number','policy_name','duration','policy_details')
admin.site.register(policy_plan_details,policy_plan)

class feedback(admin.ModelAdmin):
    list_display=('id','to','title','feedback_msg','date')
admin.site.register(feedback_table,feedback)

class insurance_company(admin.ModelAdmin):
    list_display=('id','insurance_name','insurance_address','insurance_city','insurance_contact_no','website','email_id')
admin.site.register(insurance_company_details,insurance_company)

class agent(admin.ModelAdmin):
    list_display=('id','company_id','agent_name','dob','gender','address','city','contact_no','email')
admin.site.register(agent_details,agent)

class policy(admin.ModelAdmin):
    list_display=('id','customer_policy_id','paid_amount','paid_data')
admin.site.register(policy_payments,policy)

class vehicle(admin.ModelAdmin):
    list_display=('id','customer_id','customer_policy_id','claim_type','vehicle_number','vehicle_name','vehicle_value','vehicle_condition','image_1','image_2','image_3','status')
admin.site.register(vehicle_claim,vehicle)


