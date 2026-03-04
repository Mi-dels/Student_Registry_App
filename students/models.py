from django.db import models

# Create your models here.
class Students(models.Model):
   
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField( )
    email= models.EmailField(null=True)
    gender = models.CharField(max_length=10, null=True )
    department = models.TextField( max_length= 100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.firstname} {self.lastname}"


