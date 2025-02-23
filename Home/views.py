from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
# Create your views here.


def home(request):
    context={
        "Page_Title":"ToDo-X",
        "Page_Heading":"ToDo-X",
    }
    return render(request, "home\index.html",context)


def signup_user(request):
    context={
        "Page_Title":"ToDo-X",
        "Page_Heading":"ToDo-X",
    }
    if request.method =="POST":
        data=request.POST
        
        First_Name=data.get("first_name")
        Last_Name=data.get("last_name")
        Username=data.get("username")
        Email=data.get("email")
        Password=data.get("confirm_password")
        print(f" 1.{First_Name} {Last_Name}\n{Username}\n{Email}\n{Password}\n\n")
        
        if User.objects.filter(username=Username).exists():
            messages.info(request, "Username already taken!!")
            return redirect("/signup/")
        
        elif User.objects.filter(email=Email).exists():
            messages.info(request, "Email address already in use!!")
            return redirect("/signup/")
        else:
            try:
                user=User.objects.create(
                    first_name=First_Name,
                    last_name=Last_Name,
                    username=Username,
                    email=Email
                )
                user.set_password(Password)
                user.save()
                
                messages.info(request,"Account Creation Successful")
                return redirect("/login/")
                
            except:
                messages.info(request,"Something went Wrong!!")
                return redirect("/signup/")
            
    return render(request, "authentication/signup_page.html",context)

def login_user(request):
    context={
        "Page_Title":"ToDo-X",
        "Page_Heading":"ToDo-X",
    }
    if request.method=="POST":
        data=request.POST
        
        Username=data.get("username")
        Password=data.get("password")
        
        user = authenticate(username=Username,password=Password)
        
        if user is not None:
            login(request,user)
            
            messages.info(request, "Login Successful!!")
            return redirect("/dashboard/")
        else:
            messages.info(request, "Invalid Credintials!!")
            return redirect("/login/")
        
    return render(request, "authentication/login_page.html",context)


def logout_user(request):
    logout(request)
    
    messages.info(request, "logout Successful!!")
    return redirect("/home/")

#-------------------------------------------------------------------
@login_required(login_url="/login/")
def dashboard(request):
    
    Live_Tasks=[
        {'id':1, 'name':'Drink Water','description': 'Drink 1L Water'},
        {'id':2,'name':'Give water to Plants','description': 'Flowering Plant'},
        {'id':3,'name':'Write an Application','description': 'to HOD'}
    ]
    
    context={
        "Page_Title":"ToDo-X",
        "Page_Heading":"ToDo-X",
        "Live_Tasks": Live_Tasks,
        "NoOfLiveTasks": 10,
        "NoOfCompletedTasks":1,
        "MissedTasks":11
        
    }
    
    return render(request, "home\dashboard.html",context)



def add_new_task(request):
    if request.method=="POST":
        print("try to add task")