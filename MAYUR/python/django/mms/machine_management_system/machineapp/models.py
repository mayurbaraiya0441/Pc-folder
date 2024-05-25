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
    brand_status=models.CharField(max_length=200,default='True')
    def __str__(self):
        return self.brand_name






class tax(models.Model):
    tax_name=models.CharField(max_length=200)
    tax_per=models.CharField(max_length=200)
    # brand_code=models.CharField(max_length=200)
    tax_status=models.CharField(max_length=200,default='True')
    def __str__(self):
        return self.tax_name
    
    
    
    
class subcategory(models.Model):
    category_id=models.ForeignKey(category, on_delete=models.CASCADE)
    subcategory_Name=models.CharField(max_length=200)
    subcategory_img=models.ImageField(upload_to='img')
    subcategory_code=models.IntegerField()
    subcategory_status=models.CharField(max_length=200,default='True')
    def __str__(self):
        return self.subcategory_Name
    
    


class country(models.Model):
    country_name=models.CharField(max_length=200)
    country_status=models.CharField(max_length=200, default='True')
    def __str__(self):
       return self.country_name
   
   

   

class state(models.Model):
    country_id=models.ForeignKey(country, on_delete=models.CASCADE)   
    state_name=models.CharField(max_length=200)
    state_status=models.CharField(max_length=200, default='True')
    def __str__(self):
       return self.state_name
   
   
class city(models.Model):
    state_id=models.ForeignKey(state, on_delete=models.CASCADE)   
    city_name=models.CharField(max_length=200)
    city_status=models.CharField(max_length=200, default='True')
    def __str__(self):
       return self.city_name
   
   
   
   
   
class customer(models.Model):
    customer_name=models.CharField(max_length=200)
    customer_number=models.IntegerField()
    customer_email=models.CharField(max_length=200)
    customer_image=models.ImageField(upload_to='customerimage')
    customer_wpnumber=models.IntegerField()
    country_id=models.ForeignKey(country, on_delete=models.CASCADE) 
    state_id=models.ForeignKey(state, on_delete=models.CASCADE)   
    city_id=models.ForeignKey(city, on_delete=models.CASCADE)   
    customer_Address=models.CharField(max_length=200)

  

    
    
    def __str__(self):
        return self.customer_name

   
   
   
   

   
    
 