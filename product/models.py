from django.db import models

# Create your models here.

class Product(models.Model): #changed class name to singular, which is a common convention
    name = models.CharField(max_length=60)
    image_url =models.TextField(blank=True)
    type = models.CharField(max_length=60)
    brand = models.CharField(max_length=30)
    available =models.BooleanField(default=True)
    price =  models.FloatField()
    description =models.TextField(blank= True)
