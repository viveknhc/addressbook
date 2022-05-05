from tokenize import Name
from django.db import models

# Create your models here.
class AddPerson(models.Model):
    name=models.CharField(max_length=30)
    hName=models.CharField(max_length=30)
    sName=models.CharField(max_length=30)
    post=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    dist=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pin=models.CharField(max_length=30)
