from django.db import models

# Create your models here.
#create table structures here
#student: name, class, year, guardian-name
#pthon classes are like blueprints
#anytime you make adjustments in the models.py, you must make and run migrations


class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='images', default='profile.png')