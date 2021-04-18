from django.contrib import admin

# Register your models here.
from .models import Contacts,UserData
from django.contrib.auth.models import User

admin.site.register(UserData)
admin.site.register(Contacts)

