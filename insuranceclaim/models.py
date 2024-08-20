from django.db import models

# Create your models here.



class customer_details(models.Model):
    customer_firstname=models.CharField(max_length=100)
    customer_lastname=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    image=models.FileField(upload_to="images/",max_length=250,null=True,default=None)

    def __str__(self):
         return self.customer_firstname


class feedback_table(models.Model):
    to=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    feedback_msg=models.CharField(max_length=100)
    date=models.CharField(max_length=100)

class insurance_company_details(models.Model):
    insurance_name=models.CharField(max_length=100)
    insurance_address=models.CharField(max_length=100)
    insurance_city=models.CharField(max_length=100)
    insurance_contact_no=models.CharField(max_length=100)
    website=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    def __str__(self):
        return self.insurance_name

class policy_plan_details(models.Model):
    policy_number=models.CharField(max_length=100)
    policy_name=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    policy_details=models.CharField(max_length=100)
    company_id=models.ForeignKey(insurance_company_details,on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.policy_name
    

class loginform(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)
    hintq=models.CharField(max_length=100)
    hinta=models.CharField(max_length=100)

class agent_details(models.Model):
    company_id=models.ForeignKey(insurance_company_details,on_delete=models.CASCADE)
    agent_name=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    def __str__(self):
         return self.agent_name


class customer_policy(models.Model):
    customer_id=models.ForeignKey(customer_details,on_delete=models.CASCADE)
    agent_id=models.ForeignKey(agent_details,on_delete=models.CASCADE)
    policy_plan_id=models.ForeignKey(policy_plan_details,on_delete=models.CASCADE)
    total_amount=models.CharField(max_length=100)
    installment_amount=models.CharField(max_length=100)
    policy_start_date=models.CharField(max_length=100)
    policy_end_date=models.CharField(max_length=100)


class policy_payments(models.Model):
    customer_policy_id=models.ForeignKey(customer_policy,on_delete=models.CASCADE)
    paid_amount=models.CharField(max_length=100)
    paid_data=models.CharField(max_length=100)
    

    



class vehicle_claim(models.Model):
    customer_id=models.ForeignKey(customer_details,on_delete=models.CASCADE)
    customer_policy_id=models.ForeignKey(customer_policy,on_delete=models.CASCADE)
    claim_type=models.CharField(max_length=100)
    vehicle_number=models.CharField(max_length=100)
    vehicle_name=models.CharField(max_length=100)
    vehicle_value=models.CharField(max_length=100)
    vehicle_condition=models.CharField(max_length=100)
    image_1=models.FileField(upload_to="vehical/",max_length=250,null=True,default=None)
    image_2=models.FileField(upload_to="vehical/",max_length=250,null=True,default=None)
    image_3=models.FileField(upload_to="vehical/",max_length=250,null=True,default=None)
    status=models.CharField(max_length=100)


    
class claim_amount(models.Model):
    customer_policy_id=models.ForeignKey(customer_policy,on_delete=models.CASCADE)
    total_valuation=models.CharField(max_length=100)
    release_date=models.CharField(max_length=100)
    release_amount=models.CharField(max_length=100)

