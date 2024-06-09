from django.db import models

# Create your models here.
class User(models.Model): #changed class name to singular, which is a common convention
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    image =models.TextField(blank=True)