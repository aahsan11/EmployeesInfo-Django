from django.shortcuts import render,redirect
from Employees.models import employees
from EmployeesInfo import forms
from EmployeesInfo.forms import AddForm

# Create your views here.

def home(request):
  
    Employees=employees.objects.all()
    return render(request,"Home.html",{'Employees':Employees})

def AddEmployee(request):
   return render(request,"AddEmployee.html")

def DeleteEmployee(request,id):
  # qa=request.get('q')
   Employees=employees.objects.get(id=id)
   #instance=employees.objects.get(id=id)
  # instance.delete()
   Employees.delete()
   #Employees=employees.objects.all()
   #return render(request,"Home.html",{'Employees':Employees})
   return redirect('/')

def UpdateEmployee(request,id):
   Employees=employees.objects.get(id=id)
   return render(request, "UpdateEmployee.html",{'Em':Employees})
   


def SaveEmployee(request):
    
    form= AddForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    
        
    Employees=employees.objects.all()
    return render(request,"Home.html",{'Employees':Employees})


def FinalUpdate(request,id):
    Employees=employees.objects.get(id=id)
    form=AddForm(request.POST or None)
    if form.is_valid():
        form=AddForm(request.POST or None, instance=Employees)
        form.save()
        
    #    f={'form':form}
    
    #return render(request, "AddEmployee.html",{'f':form})
   
    return redirect('/')




  
         
     
   

