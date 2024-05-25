from django.shortcuts import render,redirect
from machineapp.models import*
from django.contrib.auth import authenticate,login,logout



baseurl='http://127.0.0.1:8000/'





def dashboard(request):
    return render(request, 'dashboard.html')


##################### Login Function ####################

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            # messages.success(request, f' welcome {username} !!') 
            return redirect(dashboard)

     
    return render(request, 'login.html')




def user_logout(request):
    logout(request)
    return redirect(user_login)


##################### category Function ####################

def category_show(request):
    categoryobj = category.objects.all()
    print(categoryobj)
    
    context={
        'category':categoryobj,
        'baseurl':baseurl,
    }
    print(categoryobj)
    return render(request,"category_show.html",context)

def category_add(request):
    if request.method ==  "POST":
        category_name=request.POST.get('category_name')
        print(category_name,"kjdkjsjdb")     
        category_image=request.FILES['category_image']
        category_code=request.POST.get('category_code')
        category_desc=request.POST.get('category_desc')
        # category_status=request.POST.get('category_status')
        print(request.FILES['category_image'],"kjdkjsjdb")
       
        
        category_obj=category()
        category_obj.category_name=category_name
        category_obj.category_image=category_image
        category_obj.category_code=category_code
        category_obj.category_desc=category_desc
        # category_obj.category_status=category_status
        category_obj.save()
        
        return redirect(category_show)
    return render(request,'category_add.html')



def category_update(request,id):
    if request.method == "POST":
        category_name=request.POST.get('category_name')
        try:
            category_image=request.FILES['category_image']
        except:
            pass
        category_code=request.POST.get('category_code')
        category_desc=request.POST.get('category_desc')
        # category_status=request.POST.get('category_status')
        # print(category_image)
        
        
        category_obj=category.objects.get(id=id)
        category_obj.category_name=category_name
        try:    
            category_obj.category_image=category_image
        except:
            pass
        category_obj.category_code=category_code
        category_obj.category_desc=category_desc
        # category_obj.category_status=category_status
        category_obj.save()
        
        return redirect(category_show)
    category_obj=category.objects.get(id=id)
    print(category_obj,'12345')
    context ={
        'category_obj':category_obj,
    }
    return render(request,'category_update.html',context)


def category_delete(request,id):
    category_obj=category.objects.get(id=id)
    category_obj.delete()
    return redirect(category_show)


def category_status(request, id):
    
    get_data = category.objects.get(id=id)
    
    if get_data.category_status == "True":
        get_data.category_status="False"
    else:
        get_data.category_status="True"

    get_data.save()
    return redirect(category_show)





##################### brand Function ####################

def brand_show(request):
    brandobj = brand.objects.all()
    print(brandobj)
    
    context={
        'brand':brandobj,
        'baseurl':baseurl,
    }
    print(brandobj)
    return render(request,"brand_show.html",context)

def brand_add(request):
    if request.method ==  "POST":
        brand_name=request.POST.get('brand_name')
        print(brand_name,"kjdkjsjdb")     
        brand_image=request.FILES['brand_image']
        brand_code=request.POST.get('brand_code')
        # category_desc=request.POST.get('category_desc')
        # brand_status=request.POST.get('brand_status')
        print(request.FILES['brand_image'],"kjdkjsjdb")
       
        
        brand_obj=brand()
        brand_obj.brand_name=brand_name
        brand_obj.brand_image=brand_image
        brand_obj.brand_code=brand_code
        # category_obj.category_desc=category_desc
        # brand_obj.brand_status=brand_status
        brand_obj.save()
        
        return redirect(brand_show)
    return render(request,'brand_add.html')



def brand_update(request,id):
    if request.method == "POST":
        brand_name=request.POST.get('brand_name')
        try:
            brand_image=request.FILES['brand_image']
        except:
            pass
        brand_code=request.POST.get('brand_code')
        # brand_desc=request.POST.get('brand_desc')
        # brand_status=request.POST.get('brand_status')
        # print(category_image)
        
        
        brand_obj=brand.objects.get(id=id)
        brand_obj.brand_name=brand_name
        try:    
            brand_obj.brand_image=brand_image
        except:
            pass
        brand_obj.brand_code=brand_code
        # brand_obj.brand_desc=brand_desc
        # brand_obj.brand_status=brand_status
        brand_obj.save()
        
        return redirect(brand_show)
    brand_obj=brand.objects.get(id=id)
    print(brand_obj,'12345')
    context ={
        'brand_obj':brand_obj,
    }
    return render(request,'brand_update.html',context)





def brand_delete(request,id):
    brand_obj=brand.objects.get(id=id)
    brand_obj.delete()
    return redirect(brand_show)


def brand_status(request, id):
    
    get_data = brand.objects.get(id=id)
    
    if get_data.brand_status == "True":
        get_data.brand_status="False"
    else:
        get_data.brand_status="True"

    get_data.save()
    return redirect(brand_show)



##################### Tax Function ####################


def tax_show(request):
    taxobj = tax.objects.all()
    print(taxobj)
    
    context={
        'tax':taxobj,
        'baseurl':baseurl,
    }
    print(taxobj)
    return render(request,"tax_show.html",context)

def tax_add(request):
    if request.method ==  "POST":
        tax_name=request.POST.get('tax_name')
        print(tax_name,"kjdkjsjdb")     
        tax_per=request.POST.get('tax_per')
        tax_status=request.POST.get('tax_status')
        # category_desc=request.POST.get('category_desc')
        # brand_status=request.POST.get('brand_status')
        # print(request.FILES['brand_image'],"kjdkjsjdb")
       
        
        tax_obj=tax()
        tax_obj.tax_name=tax_name
        tax_obj.tax_per=tax_per
        # tax_obj.tax_status=tax_status
        # category_obj.category_desc=category_desc
        # tax_obj.tax_status=tax_status
        tax_obj.save()
        
        return redirect(tax_show)
    return render(request,'tax_add.html')



def tax_update(request,id):
    if request.method == "POST":
        tax_name=request.POST.get('tax_name')
        # try:
            # brand_image=request.FILES['brand_image']
        # except:
            # pass
        tax_per=request.POST.get('tax_per')
        # brand_desc=request.POST.get('brand_desc')
        # tax_status=request.POST.get('tax_status')
        # print(category_image)
        
        
        
        tax_obj=tax.objects.get(id=id)
        tax_obj.tax_name=tax_name
        # try:    
            # tax_obj.tax_image=tax_image
        # except:
            # pass
        tax_obj.tax_per=tax_per
        # brand_obj.brand_desc=brand_desc
        # brand_obj.brand_status=brand_status
        tax_obj.save()
        
        return redirect(tax_show)
    tax_obj=tax.objects.get(id=id)
    print(tax_obj,'12345')
    context ={
        'tax_obj':tax_obj,
    }
    return render(request,'tax_update.html',context)





def tax_delete(request,id):
    tax_obj=tax.objects.get(id=id)
    tax_obj.delete()
    return redirect(tax_show)


def tax_status(request, id):
    
    get_data =tax.objects.get(id=id)
    
    if get_data.tax_status == "True":
        get_data.tax_status="False"
    else:
        get_data.tax_status="True"

    get_data.save()
    return redirect(tax_show)




##################### Sub Category Function ####################


def subcategory_show(request):
    subcategoryobj = subcategory.objects.all()
    print(subcategoryobj)
    
    context={
        'subcategory':subcategoryobj,
        'baseurl':baseurl,
    }
    print(subcategoryobj)
    return render(request,"subcategory_show.html",context)

def subcategory_add(request):
    if request.method ==  "POST":
        category_id=request.POST.get('category_id')
        category_obj=category.objects.get(id=category_id)
        subcategory_name=request.POST.get('subcategory_name')
        print(subcategory_name,"kjdkjsjdb")     
        subcategory_code=request.POST.get('subcategory_code')
        subcategory_image=request.FILES['subcategory_image']
        # subcategory_status=request.POST.get('subcategory_status')
        # category_desc=request.POST.get('category_desc')
        # brand_status=request.POST.get('brand_status')
        # print(request.FILES['brand_image'],"kjdkjsjdb")
        
        
       
        
        subcategory_obj=subcategory()
        subcategory_obj.subcategory_Name=subcategory_name
        subcategory_obj.subcategory_img=subcategory_image
        subcategory_obj.subcategory_code=subcategory_code
        subcategory_obj.category_id=category_obj

        

        # tax_obj.tax_status=tax_status
        # category_obj.category_desc=category_desc
        # tax_obj.tax_status=tax_status
        subcategory_obj.save()
        
        return redirect(subcategory_show)
    categoryobj =category.objects.all()
    context={
        'category':categoryobj,
        'baseurl':baseurl,
    }
    return render(request,'subcategory_add.html',context)



def subcategory_update(request,id):
    if request.method == "POST":
        subcategory_name=request.POST.get('subcategory_name')
        try:
            subcategory_image=request.FILES['subcategory_image']
        except:
            pass
        subcategory_code=request.POST.get('subcategory_code')
        # brand_desc=request.POST.get('brand_desc')
        # tax_status=request.POST.get('tax_status')
        # print(category_image)
        category_id=request.POST.get('category_id')
        category_obj=category.objects.get(id=category_id)
        
        
        
        subcategory_obj=subcategory.objects.get(id=id)
        subcategory_obj.subcategory_Name=subcategory_name
        try:    
            subcategory_obj.subcategory_img=subcategory_image
        except:
            pass
        subcategory_obj.subcategory_code=subcategory_code
        # brand_obj.brand_desc=brand_desc
        # brand_obj.brand_status=brand_status
        subcategory_obj.category_id=category_obj

        subcategory_obj.save()
        
        return redirect(subcategory_show)
    subcategory_obj=subcategory.objects.get(id=id)
    print(subcategory_obj,'12345')
    categoryobj =category.objects.all()

    context ={
        'subcategory_obj':subcategory_obj,
        'categoryobj':categoryobj,
        
    }
    return render(request,'subcategory_update.html',context)





def subcategory_delete(request,id):
    subcategory_obj=subcategory.objects.get(id=id)
    subcategory_obj.delete()
    return redirect(subcategory_show)


def subcategory_status(request, id):
    
    get_data =subcategory.objects.get(id=id)
    
    if get_data.subcategory_status == "True":
        get_data.subcategory_status="False"
    else:
        get_data.subcategory_status="True"

    get_data.save()
    return redirect(subcategory_show)




##################### country Function ####################


def country_show(request):
    country_obj = country.objects.all()
    
    
    context={
        'country':country_obj,
        'baseurl':baseurl,
    }
    return render(request,"country_show.html",context)

def country_add(request):
    if request.method ==  "POST":
        country_name=request.POST.get('country_name')
        
       
        
        country_obj=country()
        country_obj.country_name=country_name
        country_obj.save()
        
        return redirect(country_show)
    return render(request,'country_add.html')



def country_update(request,id):
    if request.method == "POST":
        country_name=request.POST.get('country_name')
          
          
          
           
        country_obj=country.objects.get(id=id)
        country_obj.country_name=country_name
        country_obj.save()
        
        return redirect(country_show)
    country_obj=country.objects.get(id=id)
    context ={
        'country_obj':country_obj,
    }
    return render(request,'country_update.html',context)


def country_delete(request,id):
    country_obj=country.objects.get(id=id)
    country_obj.delete()
    return redirect(country_show)


def country_status(request, id):
    
    get_data = country.objects.get(id=id)
    
    if get_data.country_status == "True":
        get_data.country_status="False"
    else:
        get_data.country_status="True"

    get_data.save()
    return redirect(country_show)




##################### state Function ####################



def state_show(request):
    stateobj = state.objects.all()

    
    context={
        'state':stateobj,
        'baseurl':baseurl,
    }
    print(stateobj)
    return render(request,"state_show.html",context)

def state_add(request):
    if request.method ==  "POST":
        country_id=request.POST.get('country_id')
        country_obj=country.objects.get(id=country_id)
        state_name=request.POST.get('state_name')    
        
        
       
        
        state_obj=state()
        state_obj.state_name=state_name
        state_obj.country_id=country_obj
        state_obj.save()
        
        return redirect(state_show)
    countryobj = country.objects.all()
    context={
        'country':countryobj,
        'baseurl':baseurl,
    }
    return render(request,'state_add.html',context)



def state_update(request,id):
    if request.method == "POST":
        state_name=request.POST.get('state_name')
        country_id=request.POST.get('country_id')
        country_obj=country.objects.get(id=country_id)
        
        
        
        state_obj=state.objects.get(id=id)
        state_obj.state_Name=state_name
        state_obj.country_id=country_obj

        state_obj.save()
        
        return redirect(state_show)
    state_obj=state.objects.get(id=id)
    # print(subcategory_obj,'12345')
    countryobj =country.objects.all()

    context ={
        'state_obj':state_obj,
        'countryobj':countryobj,
        
    }
    return render(request,'state_update.html',context)





def state_delete(request,id):
    state_obj=state.objects.get(id=id)
    state_obj.delete()
    return redirect(state_show)


def state_status(request, id):
    
    get_data =state.objects.get(id=id)
    
    if get_data.state_status == "True":
        get_data.state_status="False"
    else:
        get_data.state_status="True"

    get_data.save()
    return redirect(state_show)





##################### city Function ####################


def city_show(request):
    cityobj = city.objects.all()

    
    context={
        'city':cityobj,
        'baseurl':baseurl,
    }
    print(cityobj)
    return render(request,"city_show.html",context)

def city_add(request):
    if request.method ==  "POST":
        state_id=request.POST.get('state_id')
        state_obj=state.objects.get(id=state_id)
        city_name=request.POST.get('city_name')    
        
        
       
        
        city_obj=city()
        city_obj.city_name=city_name
        city_obj.state_id=state_obj
        city_obj.save()
        
        return redirect(city_show)
    stateobj = state.objects.all()
    context={
        'state':stateobj,
        'baseurl':baseurl,
    }
    return render(request,'city_add.html',context)



def city_update(request,id):
    if request.method == "POST":
        city_name=request.POST.get('city_name')
        state_id=request.POST.get('state_id')
        state_obj=state.objects.get(id=state_id)
        

        city_obj=city.objects.get(id=id)
        city_obj.city_name=city_name
        city_obj.state_id=state_obj
        city_obj.save()
        
        return redirect(city_show)
    city_obj=city.objects.get(id=id)
    stateobj=state.objects.all()

    context ={
        'city_obj':city_obj,
        'stateobj':stateobj,
        
    }
    return render(request,'city_update.html',context)





def city_delete(request,id):
    city_obj=city.objects.get(id=id)
    city_obj.delete()
    return redirect(city_show)


def city_status(request, id):
    
    get_data =city.objects.get(id=id)
    
    if get_data.city_status == "True":
        get_data.city_status="False"
    else:
        get_data.city_status="True"

    get_data.save()
    return redirect(city_show)



##################### customer Function ####################



def customer_show(request):
    customerobj = customer.objects.all()

    
    context={
        'customer':customerobj,
        'baseurl':baseurl,
    }
    print(customerobj)
    return render(request,"customer_show.html",context)

def customer_add(request):
    if request.method ==  "POST":
        customer_name=request.POST.get('customer_name')
        customer_number=request.POST.get('customer_number')
        customer_email=request.POST.get('customer_email')
        customer_image=request.FILES['customer_image']
        customer_wpnumber=request.POST.get('customer_wpnumber')
        country_id=request.POST.get('country_id')
        state_id=request.POST.get('state_id')
        city_id=request.POST.get('city_id')
        customer_address=request.POST.get('customer_address')
        
        country_obj=country.objects.get(id=country_id)
        state_obj=state.objects.get(id=state_id)
        city_obj=city.objects.get(id=city_id)
        
        
        
        
        
        
       
        
        customer_obj=customer()
        customer_obj.customer_name=customer_name
        customer_obj.customer_number=customer_number
        customer_obj.customer_email=customer_email
        customer_obj.customer_image=customer_image
        customer_obj.customer_wpnumber=customer_wpnumber
        customer_obj.country_id=country_obj
        customer_obj.state_id=state_obj
        customer_obj.city_id=city_obj
        customer_obj.customer_address=customer_address    
        customer_obj.save()
        
        return redirect(customer_show)
    countryobj = country.objects.all()
    stateobj = state.objects.all()
    cityobj = city.objects.all()
    
    context={
        'country':countryobj,
        'state':stateobj,
        'city':cityobj,
        'baseurl':baseurl,
    }
    return render(request,'customer_add.html',context)



def customer_update(request,id):
    if request.method == "POST":
        customer_name=request.POST.get('customer_name')
        try:
            customer_image=request.FILES['customer_image']
        except:
            pass
        # customer_name=request.POST.get('customer_name')
        customer_number=request.POST.get('customer_number')
        customer_email=request.POST.get('customer_email')
        customer_image=request.FILES['customer_image']
        customer_wpnumber=request.POST.get('customer_wpnumber')
        country_id=request.POST.get('country_id')
        state_id=request.POST.get('state_id')
        city_id=request.POST.get('city_id')
        customer_address=request.POST.get('customer_address')
        
        
        
        country_obj=country.objects.get(id=country_id)
        state_obj=state.objects.get(id=state_id)
        city_obj=city.objects.get(id=city_id)
        
        
        
        
        country_obj=country.objects.get(id=id)
        customer_obj.customer_name=customer_name
        try:    
            customer_obj.customer_image=customer_image
        except:
            pass
        customer_obj=customer()
        # customer_obj.customer_name=customer_name
        customer_obj.customer_number=customer_number
        customer_obj.customer_email=customer_email
        customer_obj.customer_image=customer_image
        customer_obj.customer_wpnumber=customer_wpnumber
        customer_obj.country_id=country_obj
        customer_obj.state_id=state_obj
        customer_obj.city_id=city_obj
        customer_obj.customer_address=customer_address    
        customer_obj.save()
            
       
        
        
        return redirect(customer_show)
    customer_obj=customer.objects.get(id=id)

    context ={
        'customer_obj':customer_obj,
    }
    return render(request,'customer_update.html',context)




def customer_delete(request,id):
    customer_obj=customer.objects.get(id=id)
    customer_obj.delete()
    return redirect(customer_show)

    
    