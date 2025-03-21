from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

from datetime import datetime
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
    
    
    else:
        Live_Task=Task_Table.objects.filter(user=request.user,DeadlineDate__gte=datetime.now())
        CompletedTask=Task_Table.objects.filter(user=request.user,IsComplete=1)
        NoOfPendingTasks=Task_Table.objects.filter(user=request.user,IsComplete=0,DeadlineDate__gte=datetime.now())
        
        Upcoming_3_Task=Task_Table.objects.filter(user=request.user,IsComplete=False, DeadlineDate__gte=datetime.now()).order_by('DeadlineDate')[:3]
        Missed_Task= Task_Table.objects.filter(user=request.user,IsComplete=False, DeadlineDate__lte=datetime.now()).order_by('DeadlineDate')[:3]
        MissedTaskCount= len(Task_Table.objects.filter(user=request.user,IsComplete=False, DeadlineDate__lte=datetime.now()))
        
        Work_Tasks=len(Task_Table.objects.filter(user=request.user, TaskCategory='Work'))
        Personal_Tasks=len(Task_Table.objects.filter(user=request.user,TaskCategory='Personal' ))
        Shopping_Tasks=len(Task_Table.objects.filter(user=request.user, TaskCategory='Shopping'))
        Health_Tasks=len(Task_Table.objects.filter(user=request.user, TaskCategory='Health'))
        
        print(Upcoming_3_Task)
        print(Missed_Task)
        
        context={
            "Page_Title":"ToDo-X",
            "Page_Heading":"ToDo-X",
            "Live_Tasks": Live_Task,
            "Upcoming_3_Task":Upcoming_3_Task,
            "NoOfPendingTasks":len(NoOfPendingTasks),
            "NoOfCompletedTasks": len(CompletedTask),
            "Missed_Task":Missed_Task,
            "MissedTasksCount":MissedTaskCount,
            "Work_Tasks": Work_Tasks,
            "Personal_Tasks": Personal_Tasks,
            "Health_Tasks":Health_Tasks,
            "Shopping_Tasks":Shopping_Tasks
            
            
        }
        
        return render(request, "home/dashboard.html",context)



def task_done(request,id):
    
    task=Task_Table.objects.filter(id=id).update(IsComplete=True,ComplateDateTime=datetime.now())
    name=Task_Table.objects.get(id=id).TaskName
    m=f"Task {name} Complete!!"
    
    messages.info(request, m)
    return redirect("/dashboard/")
    
    

def task_undone(request,id):
    Task_Table.objects.filter(id=id).update(IsComplete=False,ComplateDateTime=None)
    task=Task_Table.objects.get(id=id)
    
    m=f"Task {task.TaskName} make as Live Task!!"
    
    messages.info(request, m)
    return redirect("/dashboard/")

def delete_task(request,id):
    task=Task_Table.objects.get(id=id)
    
    name=task.TaskName
    task=Task_Table.objects.filter(id=id).delete()
    
    m=f"Task {name} Deteted!!"
    
    messages.info(request, m)
    return redirect("/dashboard/")

def edit_task(request,id):
    
    if request.method=='POST':
        data=request.POST
        
        TaskId=(data.get("TaskId"))
        TaskName=data.get("TaskName")
        TaskDec=data.get("TaskDec")
        DeadLine=data.get("DeadLine")
        DeadTime=data.get("DeadTime")
        Category=data.get("Category")
        Priority=data.get("Label")
        
        task=Task_Table.objects.get(id=TaskId)
        
        task.TaskName=TaskName
        task.TaskDescription=TaskDec
        task.TaskCategory=Category
        task.Label=Priority
        task.DeadlineDate=DeadLine
        task.DeadlineTime=DeadTime
        
        task.save()
        
        messages.info(request, "Task Updated")
        
        return redirect("/dashboard")
    else:
        task=Task_Table.objects.get(id=id)
        
        context={
            "Page_Title":"ToDo-X",
            "Page_Heading":"ToDo-X",
            'task': task
        }
        
        return render (request, 'home/editTask.html',context)