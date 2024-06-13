from django.db import models
from django.utils import timezone
# Create your models here.


class Todolist(models.Model):
    title=models.CharField(max_length=200)
    created_at=models.DateTimeField(default=timezone.now,blank=True)
    completed=models.BooleanField(default=False)


    def __str__(self) :
        return self.title
    
    

