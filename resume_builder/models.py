from django.db import models

class Contacts(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile_no=models.IntegerField()
    message=models.CharField(max_length=250)
    def __str__(self):
        return self.name


    


