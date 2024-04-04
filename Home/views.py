from django.shortcuts import render, redirect
from .models import Student,Exam_Result,Parent
from django.http import HttpResponse

from.forms import StudentCreationForm,UpdateStudentForm,ParentCreationForm


# Create your views here.

def index (request):
    
    info ={
        
        'name': "Sanjog",
        'age': 21,
        'location':"pkr"
        
    }
    
    contact={
        'phone':"193713100",
        'email':"sanjog14@gmail.com"
    }
    
    details={
        "information": info,
        "contact": contact,
    }
    
    
    
    return  render(request,'Home/index.html',details)

def months(request):
    
    
    month=['jan','feb','mar','apr','may','jun']
    
    
    context={
    "month": month
    }
    
    return  render(request,'Home/about.html',context)


def index (request):
    
    
    
    students = Student.objects.all()
    result = Exam_Result.objects.all()
    parents = Parent.objects.all()
    
    
    
    context={
        'students':students,
        'result':result,
        'parents':parents
    }
    return render(request,'Home/index.html', context)


# def add_student(request):
    
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         roll = request.POST.get('roll')
#         city = request.POST.get('city')
#         student = Student(name=name,roll=roll, city=city)
#         student.save()
                
#         return HttpResponse("Student Added Succesfully")
#     else:
#         return render(request,'Home/add_student.html')
    
 
def add_student(request):
    form = StudentCreationForm()
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')      
    
    return render(request,'Home/add_student.html',{"form":form})
 


def update_student(request,id):
    student=Student.objects.get(pk=id)
    form = UpdateStudentForm(instance=student)
    if request.method == 'POST':
        form = UpdateStudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('index') 
    
    return render(request,'Home/update_student.html',{"form":form})
 

def retrieve_student(request,id):
    student=Student.objects.get(pk=id)
    return render(request,'Home/retrieve.html',{'student':student})


def add_parent(request):
    form=ParentCreationForm()
    if request.method == 'POST':
        form = ParentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')        
    
    return render(request,'Home/add_parent.html',{"form":form})

def delete_student(request,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return HttpResponse("Student Deleted Successfully")


    
    
# def update_student(request,id):
#     student= Student.objects.get(pk=id)
    
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         roll = request.POST.get('roll')
#         city = request.POST.get('city')
        
#         student.name =name
#         student.roll =roll
#         student.city =city
#         student.save()
                
#         return HttpResponse("Student Update Succesfully")
#     else:
#         return render(request,'Home/add_student.html',{'student':Student})
    

    
    