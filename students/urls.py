from django.urls import path
from .views import   studentslist, studentsdetails, students_create, student_update,student_delete

urlpatterns = [

   
    path('', studentslist, name='studentslist'),
    path('Student/<int:id>/', studentsdetails, name='studentsdetails' ),
    path('addstudent/', students_create, name='students_create'),
    path('update/<int:id>/', student_update, name='student_update'),
    path('delete/<int:id>/', student_delete, name='student_delete')
]