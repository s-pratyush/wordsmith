from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contacts



def index(request):
    if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone_no') and request.POST.get('message'):
                post=Contacts()
                post.name= request.POST.get('name')
                post.message= request.POST.get('message')
                post.mobile_no=request.POST.get('phone_no')
                post.email=request.POST.get('email')
                post.save()
                print("Submitted")
    return render(request,'resume_builder/index.html')
    
def form(request):
    if request.method == 'POST':
        data={}
        data['F_name']=request.POST.get('f_name')
        data['L_name']=request.POST.get('l_name')
        data['Dob']=request.POST.get('dob')
        data['Objective']=request.POST.get('objective')
        data['Image']=request.POST.get('image')
        data['Email']=request.POST.get('email')
        data['Tel_no']=request.POST.get('tel_no')
        data['Addr_1']=request.POST.get('add_1')
        data['Addr_2']=request.POST.get('add_2')
        data['Country']=request.POST.get('country')
        data['Zipcode']=request.POST.get('zipcode')
        data['Other']=request.POST.get('richtext')
        data['skills']=request.POST.get('skills')
        print(data)
    return render(request,'resume_builder/info.html')

def cv_design(request):
    return render(request,'resume_builder/cv_design.html')    

