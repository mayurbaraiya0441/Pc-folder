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



 


    
    