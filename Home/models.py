from django.db import models
from django.contrib.auth.models import User
from datetime import time


# Create your models here.


class Task_Table(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    IsComplete=models.BooleanField(default=False)
    
    CreatedAt=models.DateTimeField(auto_now_add=True)
    
    TaskName=models.TextField()
    TaskDescription=models.TextField(default="No Description")
    TaskCategory=models.CharField(max_length=15)
    
    Label=models.CharField(max_length=25,null=True,blank=True)
    
    DeadlineDate=models.DateField()
    DeadlineTime=models.TimeField(default=time(23, 59))
    
    def __str__(self) -> str:
        return self.TaskName