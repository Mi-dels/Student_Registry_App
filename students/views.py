from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Students
from .forms import  StudentForm
from .models import Students
from rest_framework import permissions, viewsets, filters
from .serializers import  StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from students.models import Students 
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken






# class StudentViewSet(viewsets.ModelViewSet):
#   queryset = Students.objects.all()
#   serializer_class = StudentSerializer
#   permission_classes = [permissions.AllowAny]

#   filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#   filterset_fields = ['gender','department']
#   search_fields = ['firstname', 'lastname', 'email']
#   ordering_fields = ['age', 'created_at']
#   ordering = ['-created_at']







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

# class SignupViewSet(viewsets.ModelViewSet):
#   queryset = Signup.objects.all()
#   serializer_class = SignupSerializer


# @api_view(['GET'])
# def Home(request):
#   return Response("hello world")


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def myprotectedroute(request):
#   return Response('You have been granted permission to my protected route')



# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = TokenObtainPairSerializer

#     def post(self, request, *args, **kwargs):

#         # Proceed with the parent method to handle token generation
#         try:
#             response = super().post(request, *args, **kwargs)
#         except TokenError as e:
#             raise InvalidToken(e.args[0])

#         # get username from form submission
#         username = request.data.get('username')
#         if username:
#             # Add user details to the response

#             user = Signup.objects.get(username=username)
#             user_serializer =  SignupSerializer(user) 

#             response.data['user'] = user_serializer.data

#         return response


    
   
   
    
   


