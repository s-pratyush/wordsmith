from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contacts 
from .models import data 
import json



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

data={}
data['F_name']="Pratyush"
data['L_name']="Saxena"
data['Dob']="12/09/2001"
data['Image']="This is image"
data['Email']="saxena18prats@gmail.com"
data['Tel_no']="9876765454"
data['Addr_1']="H.No 12 , XYZ street"
data['Addr_2']="ABC Villa"
data['Country']="India"
data['Zipcode']="262001"
data['Other']="Here is other text"
data['skills']=['go','cpp','c','c#','python']
def form(request):
    if request.method == 'POST':
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
        edu=request.POST.getlist('Education')
        edu_list=[]
        for e in edu:
            edu_list.append(e.split(','))
        data['Education']=edu_list
        exp=request.POST.getlist('Experiance')
        exp_list=[]
        for e in exp:
            exp_list.append(e.split(','))
        data['Experiance']=exp_list
        print(edu_list)
        skillset=[]
        for s in request.POST.get('skills').split(','):
            skillset.append(s)
        data['skills']=skillset
        return render(request,'resume_builder/srt-resume.html',{'data':data})
    return render(request,'resume_builder/info.html')

def cv_design(request):
    return render(request,'resume_builder/cv_design.html')    

def resume(request):
    return render(request,'resume_builder/srt-resume.html',{'data':data})