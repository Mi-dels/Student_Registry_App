from django.db import models

# Create your models here.
class Students(models.Model):

    class Gender (models.TextChoices): 
      Male =  'M','Male'
      Female =  'F','Female'
      Others = 'O','Others'
    
   
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField( )
    email= models.EmailField(null=True)
    gender = models.CharField( max_length= 10, choices= Gender.choices, null=True)
    department = models.TextField( max_length= 100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.firstname} {self.lastname}"


