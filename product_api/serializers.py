from rest_framework import serializers
from .models import Product, ProductImage, ProductCategory, CustomizedProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class CustomizedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizedProduct
        fields = '__all__'