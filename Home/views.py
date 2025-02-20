from django.shortcuts import render

# Create your views here.




def home(request):
    
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
    
    return render(request, "home\index.html",context)
