from django.db import models
import datetime
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class News(models.Model):
    title = models.CharField(max_length=200)
    descreption = models.CharField(max_length=500)
    catagory = models.ForeignKey(Category,on_delete=models.CASCADE , default=1)
    image = models.ImageField(upload_to='uploads/products')
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title   


class ContactData(models.Model):
    name = models.CharField(max_length=100) 
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField(max_length=254) 
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    

class AdminPost(models.Model):
    title = models.CharField(max_length=100)    
    Description = models.CharField(max_length=100)    
    
    def __str__(self):
        return self.title