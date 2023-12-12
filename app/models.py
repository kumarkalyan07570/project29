from django.db import models

# Create your models here.

from app.models import *



class Kalyan(models.Model):
    First_Name=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)


    def __str__(self):
        return self.LastName


class Sam(models.Model):
    First_Name=models.ForeignKey(Kalyan,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    url=models.URLField()
    

    def __str__(self):
        return self.name
    















    
    






