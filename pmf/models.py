from django.db import models

# Create your models here.
class query_students(models.Model):
    name= models.CharField('user name' ,max_length=30)
    email = models.EmailField('user email', max_length=256)
    phone = models.CharField('user email', max_length=10)
    coaching = models.CharField('user email', max_length=80)