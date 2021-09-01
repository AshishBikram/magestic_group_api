from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer, ProductImageSerializer, ProductCategorySerializer
from .models import Product, ProductImage, ProductCategory
from django.conf import settings as api_settings
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from django.http import Http404


# Create your views here.
class ProductCLView(APIView):
    permission_classes = (IsAdminUser,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        paginator = LimitOffsetPagination()
        page = paginator.paginate_queryset(self.queryset, request)
        serializer = self.serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class ProductPGDView(APIView):
    permission_classes = (IsAdminUser,)
    serializer_class = ProductSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = self.serializer_class(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = self.serializer_class(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductImageCLView(APIView):
    permission_classes = (IsAdminUser,)
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = ProductImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        paginator = LimitOffsetPagination()
        page = paginator.paginate_queryset(self.queryset, request)
        serializer = self.serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class ProductImagePGDView(APIView):
    permission_classes = (IsAdminUser,)
    serializer_class = ProductImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return ProductImage.objects.get(pk=pk)
        except ProductImage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product_image = self.get_object(pk)
        serializer = self.serializer_class(product_image)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product_image = self.get_object(pk)
        serializer = self.serializer_class(product_image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product_image = self.get_object(pk)
        product_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductCategoryCLView(APIView):
    permission_classes = (IsAdminUser,)
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        paginator = LimitOffsetPagination()
        page = paginator.paginate_queryset(self.queryset, request)
        serializer = self.serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class ProductCategoryPGDView(APIView):
    permission_classes = (IsAdminUser,)
    serializer_class = ProductCategorySerializer

    def get_object(self, pk):
        try:
            return ProductCategory.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product_category = self.get_object(pk)
        serializer = self.serializer_class(product_category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product_category = self.get_object(pk)
        serializer = self.serializer_class(product_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product_category = self.get_object(pk)
        product_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)