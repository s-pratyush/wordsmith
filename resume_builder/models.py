from django.db import models

class Contacts(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile_no=models.IntegerField()
    message=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class data(models.Model):
    F_name=models.CharField(max_length=100)
    L_name=models.CharField(max_length=100)
    Dob=models.DateField()
    Objective=models.CharField(max_length=250)
    Image=models.ImageField()
    Email=models.EmailField(null=True)
    Tel_no=models.CharField(max_length=10)
    Addr_1=models.CharField(max_length=250)
    Addr_2=models.CharField(max_length=250)
    Country=models.CharField(max_length=50)
    Zipcode=models.CharField(max_length=6)
    Other=models.CharField(max_length=1000,null=True)
    skills=models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.Email




    


