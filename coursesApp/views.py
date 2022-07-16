from django.shortcuts import render, HttpResponse ,redirect
from .models import Course

def index(request):
    context= {
        'Course':Course.objects.all()
        }
    return render(request,"index.html",context)

def add_course (request):
    if request.method == 'POST':
        Course.objects.create(
            name= request.POST["name"],
            Description= request.POST["Description"],
        )
    return redirect("/")

def delete_course(request,id):
    context= {
        'Course':Course.objects.get(id=id)
    }
    return render (request,"index2.html",context)

def remove(request,id):
    ThisCourse =Course.objects.get(id=id)
    ThisCourse.delete()
    return redirect("/")