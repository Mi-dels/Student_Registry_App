from django.urls import path
from .views import   studentslist, studentsdetails

urlpatterns = [

   
    path('', studentslist, name='studentslist'),
    path('Student/<int:id>/', studentsdetails, name='studentsdetails' )
]