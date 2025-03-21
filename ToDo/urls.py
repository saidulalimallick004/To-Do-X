"""
URL configuration for ToDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from Home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #---------------------------------------------------------------------------------------
    
    path('',home,name='Home'),
    path('home/',home,name='Home'),
    
    #---------------------------------------------------------------------------------------
    
    path('signup/',signup_user, name="Sign-Up"),
    path('login/',login_user, name="Login"),
    path('logout/',logout_user, name="Logout"),
    
    #---------------------------------------------------------------------------------------
    
    path('dashboard/',dashboard,name='Dashboard'),
    path('completeTask/<int:id>',task_done, name="DoneTask"),
    path('undoTask/<int:id>',task_undone, name="UndoneTask"),
    path('editTask/<int:id>',edit_task,name='Edit Task'),
    path('deleteTask/<int:id>',delete_task,name='Delete Task'),
    
    
]
