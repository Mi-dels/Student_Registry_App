from django.db import models

# Create your models here.
class Students(models.Model):
   
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField( )
    email= models.EmailField(null= True)
    gender = models.CharField(max_length=10, null= True )
    deparment = models.TextField(null= True)


    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.department}"