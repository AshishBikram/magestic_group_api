from django.db import models
from product.models import Product
# Create your models here.


class Description(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=255)
    title_detail = models.CharField(max_length=10000)
