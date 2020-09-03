from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contacts



def index(request):
    return render(request,'resume_builder/index.html')
def form(request):
    return render(request,'resume_builder/form.html')

def Submit_message(request):
        if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone_no') and request.POST.get('message'):
                post=Contacts()
                post.name= request.POST.get('name')
                post.message= request.POST.get('message')
                post.mobile_no=request.POST.get('phone_no')
                post.email=request.POST.get('email')
                post.save()
                return  

        else:
                return render(request,'posts/create.html')


