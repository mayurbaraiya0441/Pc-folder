from django.db import models

# Create your models here.

class category(models.Model):
    category_name=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='categoryimage')
    category_code=models.CharField(max_length=200)
    category_desc=models.CharField(max_length=200,null=False)
    category_status=models.CharField(max_length=200, default='True')
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
       return self.category_name
    
