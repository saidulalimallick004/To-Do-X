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
    return render(request, "home/index.html",context)


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
    
    if request.method=="POST":
        data=request.POST
        
        TaskName=data.get("TaskName")
        TaskDec=data.get("TaskDec")
        
        DeadLine=data.get("DeadLine")
        DeadTime=data.get("DeadTime")
        
        Category=data.get("Category")
        Priority=data.get("Label")
        
        
        task=Task_Table.objects.create(
            user=request.user,
            TaskName=TaskName,
            TaskDescription=TaskDec,
            
            TaskCategory=Category,
            Label=Priority,
            
            DeadlineDate=DeadLine,
            DeadlineTime=DeadTime,
        )
        
        task.save()
        messages.info(request, "Task Created")
        
        return redirect('/dashboard/')
           
    Live_Task=Task_Table.objects.filter(user=request.user)
    CompletedTask=Task_Table.objects.filter(user=request.user,IsComplete=1)
    NoOfPendingTasks=Task_Table.objects.filter(user=request.user,IsComplete=0)
    
    context={
        "Page_Title":"ToDo-X",
        "Page_Heading":"ToDo-X",
        "Live_Tasks": Live_Task,
        "NoOfPendingTasks":len(NoOfPendingTasks),
        "NoOfCompletedTasks": len(CompletedTask),
        "MissedTasks":11
    }
    
    return render(request, "home/dashboard.html",context)



def task_done(request,id):
    
    task=Task_Table.objects.filter(id=id).update(IsComplete=True)
    
    m=f"Task {id} Complete!!"
    
    messages.info(request, m)
    return redirect("/dashboard/")
    