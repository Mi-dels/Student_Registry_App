from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Students

# def students(request):
#   template = loader.get_template('studentsdetails.html')
#   return HttpResponse(template.render())


def home(request):
  return HttpResponse('Welcome To The Home Page')




def studentslist(request):  
  mystudents = Students.objects.all().values()
  return render(request,'studentslist.html', {'mystudents': mystudents})


def studentsdetails(request, id ):
    student = get_object_or_404(Students, id=id)
    return render(request, 'studentsdetails.html', {'student': student})
    
   

# Create your views here.
