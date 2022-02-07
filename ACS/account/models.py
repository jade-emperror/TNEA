import email
from pyexpat import model
from django.db import models

# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100,null=False)
    lname = models.CharField(max_length=100,null=True,blank=True,default="")
    email = models.EmailField(max_length=75,null=False)
    pwd = models.CharField(max_length=200,null=False)
    phoneno = models.CharField(max_length=15,null=True)