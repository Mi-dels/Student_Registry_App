from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Students
from .forms import  StudentForm
from .models import Students
from rest_framework import permissions, viewsets, filters
from .serializers import  StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend



class StudentViewSet(viewsets.ModelViewSet):
  queryset = Students.objects.all()
  serializer_class = StudentSerializer
  permission_classes = [permissions.AllowAny]

  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  filterset_fields = ['gender','department']
  search_fields = ['firstname', 'lastname', 'email']
  ordering_fields = ['age', 'created_at']
  ordering = ['-created_at']







# def studentslist(request):  
#   mystudents = Students.objects.all().values()
#   return render(request,'studentslist.html', {'mystudents': mystudents})


# def studentsdetails(request, id ):
#     student = get_object_or_404(Students, id=id)
#     return render(request, 'studentsdetails.html', {'student': student})



# def students_create(request):
#   if request.method == "POST":
#     form = StudentForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect('studentslist') 
  
#   else:
#     form = StudentForm()

#     return render(request, "studentcreate.html", {"form" : form})
  


# def student_update(request, id):
#   Stu_dent = get_object_or_404(Students, id=id)
#   if request.method == "POST":
#     form = StudentForm(request.POST, instance=Stu_dent)
#     if form.is_valid():
#       form.save()
#       return redirect('studentslist') 
    
#   else:
#     form = StudentForm(instance=Stu_dent)

#     return render(request, "studentcreate.html", {"form" : form})



# def student_delete(request, id):
#   students = get_object_or_404(Students, id=id)
#   students.delete()
#   return redirect('studentslist')

    
   
   
    
   


