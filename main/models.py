from pydoc import describe
from django.db import models

class task(models.Model):
    title = models.CharField(max_length=50)
    tasks = models.TextField(max_length=100,default=" ")

    def __str__(self):
        return self.title

class Book(models.Model):
    name = models.CharField(max_length=50)
    Address =models.CharField(max_length=30, default='')
    email =models.EmailField(blank = True)
    describe = models.TextField(default = '')
    def __str__(self):
        return self.name

class test(models.Model):
    hobby = models.CharField(max_length=100)
    
class sport(models.Model):
    length = models.IntegerField()
class Emp(models.Model):
    name = models.CharField(max_length=255,verbose_name="name")
    age = models.IntegerField(verbose_name="age")
    salary = models.DecimalField(decimal_places=10,max_digits=100000000000,verbose_name="salary")
    email =models.EmailField(blank = True)
    number=models.IntegerField(verbose_name="number")
    country=models.CharField(max_length=255,verbose_name="country")   
