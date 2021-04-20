from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from .models import Contacts
from .models import UserData,subscription
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
import json
import razorpay


def index(request):
    if request.method == "POST":
        if (
            request.POST.get("name")
            and request.POST.get("email")
            and request.POST.get("phone_no")
            and request.POST.get("message")
        ):
            post = Contacts()
            post.name = request.POST.get("name")
            post.message = request.POST.get("message")
            post.mobile_no = request.POST.get("phone_no")
            post.email = request.POST.get("email")
            post.save()
            print("Submitted")
    return render(request, "resume_builder/index.html")


def signup(request):
    if request.method == "POST":
        user = User.objects.create_user(
            request.POST.get("username"),
            request.POST.get("mail"),
            request.POST.get("pass"),
        )
        user.save()
        sub=subscription.objects.create(
            user=user
        )
        print("hello done !")
        return redirect('/login')
    return render(request, "resume_builder/sign_up.html")


def log_in(request):
    if request.user.is_authenticated:
        print("IS AUTHENTICATED")
        username=request.user.username
        return redirect('/myprofile')
    else:
        print("sorry")
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get("username"), password=request.POST.get("pass")
        )
        if user is not None:
            print("hurray logedd in :) \n")
            username = user.username
            django_login(request,user)
            email=request.user.email
            count=len(UserData.objects.filter(username=username))
            return redirect('/myprofile')
        else:
            print("Paradon unable to login :( ")
    return render(request, "resume_builder/login.html")


def logout(request):
    django_logout(request)
    return  redirect('/login')

def myprofile(request):
    username = request.user.username
    email=request.user.email
    count=len(UserData.objects.filter(username=username))
    sub=subscription.objects.filter(user=request.user).values()[0]['subscribed']
    client = razorpay.Client(auth = ('rzp_test_d20UU7vPPDYgxU', 'apIp3rRDKlg0cSkqO9G9ffJ4'))
    payment_order = client.order.create(dict(amount=100,currency='INR'))
    order_id = payment_order['id']
    order_status = payment_order['status']
    if order_status == 'created':
        payment_order['name']=username
        payment_order['email']=email
        return render(request,"resume_builder/myprofile.html",{"username":username,"email":email,"count":count,"payment":payment_order,"subscription":sub})
    return render(request,"resume_builder/myprofile.html",{"username":username,"email":email,"count":count})

def payment_status(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    # client instance
    client = razorpay.Client(auth = ('rzp_test_d20UU7vPPDYgxU', 'apIp3rRDKlg0cSkqO9G9ffJ4'))

    try:
        status=False
        status = client.utility.verify_payment_signature(params_dict)
        subscription.objects.filter(user=request.user).update(subscribed=True)
        return render(request, 'resume_builder/payment_status.html', {'status': True})
    except:
        return render(request, 'resume_builder/payment_status.html', {'status': False})

def forgotpass(request):
    status=""
    if request.method == "POST":
        mail = request.POST.get("mail")
        emails = (
            User.objects.filter(is_active=True)
            .exclude(email="")
            .values_list("email", flat=True)
        )
        if mail in emails:
            status = "We have sent Password Reset link to your email"
        else:
            status= "*Email is not registered."
        print(emails)
    return render(request, "resume_builder/forgotpass.html",{"status":status})


def loadindb(request,data):
    try:
        User = UserData()
        User.Email = data["Email"]
        User.F_name = data["F_name"]
        User.L_name = data["L_name"]
        User.Dob = data["Dob"]
        User.Tel_no = data["Tel_no"]
        User.Addr_1 = data["Addr_1"]
        User.Addr_2 = data["Addr_2"]
        User.Country = data["Country"]
        User.Zipcode = data["Zipcode"]
        User.skills = data["skills"]
        User.edu = data["Education"]
        User.exp = data["Experiance"]
        User.Objective = data["Objective"]
        User.username=request.user.username
        User.save()
    except:
        print("There is an error in loading into database")


data = {}  # default values for testing
data["F_name"] = "Pratyush"
data["L_name"] = "Saxena"
data["Dob"] = "12/09/2001"
data["Image"] = "This is image"
data["Email"] = "saxena18prats@gmail.com"
data["Tel_no"] = "9876765454"
data["Addr_1"] = "H.No 12 , XYZ street"
data["Addr_2"] = "ABC Villa"
data["Country"] = "India"
data["Zipcode"] = "262001"
data["Other"] = "Here is other text"
data["skills"] = ["go", "cpp", "c", "c#", "python"]


def form(request):
    if request.method == "POST":
        data["F_name"] = request.POST.get("f_name")
        data["L_name"] = request.POST.get("l_name")
        data["Dob"] = request.POST.get("dob")
        data["Objective"] = request.POST.get("objective")
        data["Image"] = request.POST.get("image")
        data["Email"] = request.POST.get("email")
        data["Tel_no"] = request.POST.get("tel_no")
        data["Addr_1"] = request.POST.get("add_1")
        data["Addr_2"] = request.POST.get("add_2")
        data["Country"] = request.POST.get("country")
        data["Zipcode"] = request.POST.get("zipcode")
        edu = request.POST.getlist("Education")
        edu_list = []
        for e in edu:
            edu_list.append(e.split(","))
        data["Education"] = edu_list
        exp = request.POST.getlist("Experiance")
        exp_list = []
        for e in exp:
            exp_list.append(e.split(","))
        data["Experiance"] = exp_list
        print(edu_list)
        skillset = []
        for s in request.POST.get("skills").split(","):
            skillset.append(s)
        data["skills"] = skillset
        loadindb(request,data)
        return render(request, "resume_builder/srt-resume.html", {"data": data})
    return render(request, "resume_builder/info.html")


def cv_design(request):
    return render(request, "resume_builder/cv_design.html")


def resume(request):
    return render(request, "resume_builder/srt-resume.html", {"data": data})

