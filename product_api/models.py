import uuid
import jsonfield
import os

from django.db import models


def user_directory_path(instance, filename):
    return os.path.join("static", "uploaded", str(instance.product_id), filename)


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    weight = models.CharField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=225, null=True, blank=True)
    categories = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=100, null=True, blank=True)
    sub_descriptions = jsonfield.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)