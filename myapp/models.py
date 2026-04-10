from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=40)

def __str__(self):
    return self.name 

# Teacher Table

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=15)

def __str__(self):
    return self.name    


