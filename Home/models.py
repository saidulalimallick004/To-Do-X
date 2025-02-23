from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task_Table(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    IsComplete=models.BooleanField()
    TaskIcon=models.TextField(null=True,blank=True)
    
    CreatedAt=models.DateTimeField(auto_now_add=True)
    
    TaskName=models.TextField()
    TaskDescription=models.TextField()
    TaskCategory=models.CharField(max_length=15)
    
    Label=models.CharField(max_length=25)
    
    DeadlineDate=models.DateField()
    DeadlineTime=models.TimeField(null=True,blank=True)
    
    
    def __str__(self) -> str:
        return self.id