from django.db import models

# Create your models here.

class Employees(models.Model):
    f_name=models.CharField(max_length=200)
    l_name=models.CharField(max_length=100)
    
    def __str__(self):
       return self.f_name
    
    