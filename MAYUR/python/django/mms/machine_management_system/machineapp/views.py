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






 


    
    