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
    weight = models.FloatField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=225, null=True, blank=True)
    categories = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True)
    sub_descriptions = jsonfield.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product_images')
    created_at = models.DateTimeField(auto_now_add=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    brand = models.CharField(max_length=255, null=False, blank=False)
    nav_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class CustomizedProduct(models.Model):
    best_sellers = jsonfield.JSONField(default=[])
    new_products = jsonfield.JSONField(default=[])
    sale_products = jsonfield.JSONField(default=[])
    created_at = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    mobile_no = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    subject = models.CharField(max_length=250, null=False, blank=False)
    message = models.TextField(null=False, blank=False)