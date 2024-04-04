from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    
    def __str__(self):
       return self.name


"""
CREATE TABLE Student  name varchar(100), roll int, city varchar(100)

"""   

class Parent(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
    
    
     
class Exam_Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    
    percentage = models.FloatField()
    garde=models.CharField(max_length=10)
    
    def __str__(self):
        return self.student.name






