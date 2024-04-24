from django.shortcuts import render,redirect
from members.models import Employees

def index(request):
    emp = Employees.objects.all()
    
    context={
        'emp':emp,
    }
    
    return render(request,"index.html",context)


def add(request):
    if request.method ==  "POST":
        firstname=request.POST.get('f_name')
        lastname=request.POST.get('l_name')
        emp=Employees()
        emp.f_name=firstname
        emp.l_name=lastname
        emp.save()
        
        return redirect(index)
    return  render(request,'add.html')



def update(request,id):
    if request.method == "POST":
        firstname=request.POST.get('f_name')
        lastname=request.POST.get('l_name')
        emp=Employees.objects.get(id=id)
        emp.f_name=firstname
        emp.l_name=lastname
        emp.save()
        # return index(request)
        return redirect(index)
    emp=Employees.objects.get(id=id)
    context ={
        'emp':emp,
    }
    return render(request,'update.html',context)

def delete_user(request,id):
    emp=Employees.objects.get(id=id)
    emp.delete()
    return redirect(index)
    
 
        
    




