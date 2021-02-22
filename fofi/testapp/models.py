from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    marks=models.IntegerField()
    hero=models.CharField(max_length=30)
    heroin=models.CharField(max_length=30)