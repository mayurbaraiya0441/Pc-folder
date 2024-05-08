from django.shortcuts import render,redirect
from members.models import Employees
from django.contrib.auth import authenticate,login,logout


def dashboard(request):
    return render(request, 'dashboard.html')


####################### user function #######################

def user_show(request):
    emp = Employees.objects.all()
    
    context={
        'emp':emp,
    }
    
    return render(request,"user_show.html",context)


def user_add(request):
    if request.method ==  "POST":
        firstname=request.POST.get('f_name')
        lastname=request.POST.get('l_name')
        emp=Employees()
        emp.f_name=firstname
        emp.l_name=lastname
        emp.save()
        
        return redirect(user_show)
    return  render(request,'user_add.html')



def user_update(request,id):
    if request.method == "POST":
        firstname=request.POST.get('f_name')
        lastname=request.POST.get('l_name')
        emp=Employees.objects.get(id=id)
        emp.f_name=firstname
        emp.l_name=lastname
        emp.save()
        # return index(request)
        return redirect(user_show)
    emp=Employees.objects.get(id=id)
    context ={
        'emp':emp,
    }
    return render(request,'user_update.html',context)

def user_delete(request,id):
    emp=Employees.objects.get(id=id)
    emp.delete()
    return redirect(user_show)



###################### Login Function ####################

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



def signin(request):
    if request.method=="POST":
       username = request.POST['username']
       pasword =  request.POST['password']
    
       
    return render(request,"login.html")

def user_logout(request):
    logout(request)
    return redirect(user_login)
 


    
    
 
        
    




