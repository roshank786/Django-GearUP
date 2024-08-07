from django.db import models

# Create your models here.


class Brand(models.Model):
     
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)



class Car(models.Model):

    company = models.ForeignKey(Brand,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    fuel = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    price = models.PositiveBigIntegerField()