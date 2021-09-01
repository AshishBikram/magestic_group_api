from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    size = models.CharField(max_length=225)
    category = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
