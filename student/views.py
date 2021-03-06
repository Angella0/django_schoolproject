from django.shortcuts import redirect, render
from.models import Student
from .forms import StudentRegistrationForm
from django.shortcuts import render
from django .urls import reverse

def register_student(request):
    if request.method == "POST":
       form = StudentRegistrationForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('student:student_list')
       else:
           print(form.errors)

    else:
        form = StudentRegistrationForm()
    return render(request, "register_student.html", {"form":form})

def student_list(request):
    students = Student.objects.all()
    return render(request,"student_list.html", {
        "students":students
    })

def student_profile(request, id):
    students = Student.objects.get(id=id)
    return render(request, "student_profile.html", {"students":students})

def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method=="POST":
        form = StudentRegistrationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_profile", id = student.id)
    else:
         form = StudentRegistrationForm(instance=student)
         return render(request, "edit_student.html", {"form":form})


       

# Create your views here.
