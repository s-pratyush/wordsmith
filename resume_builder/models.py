from django.db import models
from django.contrib.auth.models import User
import jsonfield
class Contacts(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile_no=models.IntegerField()
    message=models.CharField(max_length=250)
    def __str__(self):
        return self.email

class subscription(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

class UserData(models.Model):
    F_name=models.CharField(max_length=100)
    L_name=models.CharField(max_length=100)
    Dob=models.DateField()
    Objective=models.CharField(max_length=250)
    Image=models.ImageField(null=True)
    Email=models.EmailField(null=True)
    Tel_no=models.CharField(max_length=10)
    Addr_1=models.CharField(max_length=250)
    Addr_2=models.CharField(max_length=250)
    Country=models.CharField(max_length=50)
    Zipcode=models.CharField(max_length=6)
    skills=jsonfield.JSONField(null=True)
    edu=jsonfield.JSONField(null=True)
    exp=jsonfield.JSONField(null=True)
    username=models.CharField(null=True,max_length=50)
    payment_status=models.BooleanField(default=False)
    def __str__(self):
        return self.Email




    


