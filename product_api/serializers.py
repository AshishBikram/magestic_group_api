from rest_framework import serializers
from .models import Product, ProductImage, ProductCategory, CustomizedProduct


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class CustomizedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizedProduct
        fields = '__all__'