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
   
   
   
   
   
class brand(models.Model):
    brand_name=models.CharField(max_length=200)
    brand_image=models.ImageField(upload_to='categoryimage')
    brand_code=models.CharField(max_length=200)
    brand_status=models.CharField(max_length=200)
    def __str__(self):
        return self.brand_name






class tax(models.Model):
    tax_name=models.CharField(max_length=200)
    tax_per=models.CharField(max_length=200)
    # brand_code=models.CharField(max_length=200)
    tax_status=models.CharField(max_length=200)
    def __str__(self):
        return self.tax_name