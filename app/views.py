from django.shortcuts import render
from random import randint
from .models import *

def Indexpage(req):
    return render(req, "app/index.html")

def Register(req):
    return render(req, "app/signup.html")

def RegisterUser(req):
    if req.POST['role'] == "Candidate":
        name = req.POST['name']
        contact = req.POST['contact']
        email = req.POST['email']
        password = req.POST['password']
        role = req.POST['role']

        user = Users.objects.filter(email=email)

        if user:
            message = "User already exists!"
            return render(req, "app/signup.html", {'msg': message})
        else:
            otp = randint(100000, 999999)

            newUser = Users.objects.create(role=role, otp=otp, email=email, password=password)
            newCandidate = Candidate.objects.create(user_id=newUser, name=name)

            return render(req, "app/otp.html")
    else:
        company_name = req.POST['name']
        contact = req.POST['contact']
        email = req.POST['email']
        password = req.POST['password']
        role = req.POST['role']
        
        company = Users.objects.filter(email=email)
        if(company):
            return render (req,"app/signup.html",{'msg':"Company already exists"})
        else:
            otp = randint(100000,999999)
            
            newUser = Users.objects.create(role=role,otp=otp,password=password)
            newCompany = Company.objects.create(user_id=newUser,company_name = company_name)
            return render(req,"app/otp.html")
        
        
def OTP(req):
    return render(req,"app/otp.html")

def verifyOTP(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        otp = req.POST.get('otp')
        user = Users.objects.get(email=email)
        if user:
            if user.otp == otp:
                return render(req, "app/login.html", {'msg': "OTP verified successfully"})
            else:
                return render(req, "app/otp.html", {'msg': "Incorrect OTP"})
        else:
            return render(req, "app/signup.html")
    else:
        return render(req, "app/otp.html")
    
def login(req):
    return render(req,"app/login.html")