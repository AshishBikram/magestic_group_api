from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer, ProductImageSerializer, ProductCategorySerializer,\
    CustomizedProductSerializer
from .models import Product, ProductImage, ProductCategory, CustomizedProduct
from django.conf import settings as api_settings
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from django.http import Http404


def get_formatted_data(data_type, value):
    if data_type == "FloatField":
        return float(value)
    elif data_type == "IntegerField":
        return int(value)
    elif data_type == "BooleanField":
        return bool(value)
    else:
        return value


def get_search_filter(fields, request):
    return {field: get_formatted_data(fields[field], request.GET[field]) for field in fields if request.GET.get(field)}


# Create your views here.
class ProductCLView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductSerializer
    fields = {field.name: field.get_internal_type() for field in Product._meta.get_fields()}

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        paginator = LimitOffsetPagination()
        search = {}
        search.update(get_search_filter(self.fields, request))
        if request.GET.get("low_price"):
            search["price__range"] = (request.GET.get("low_price"), request.GET.get("high_price", 99999999999))
        page = paginator.paginate_queryset(Product.objects.filter(**search), request)
        serializer = self.serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class ProductPGDView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
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
    permission_classes = (IsAuthenticatedOrReadOnly,)
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
    permission_classes = (IsAuthenticatedOrReadOnly,)
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
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductCategorySerializer
    fields = {field.name: field.get_internal_type() for field in ProductCategory._meta.get_fields()}

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        if request.GET.get("request_type") != "All":
            paginator = LimitOffsetPagination()
            search = get_search_filter(self.fields, request)
            page = paginator.paginate_queryset(ProductCategory.objects.filter(**search), request)
            serializer = self.serializer_class(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = self.serializer_class(ProductCategory.objects.all(), many=True)
            return Response(serializer.data)


class ProductCategoryPGDView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
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


class CustomizedProductCLView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CustomizedProductSerializer

    def post(self, request):
        obj = CustomizedProduct.objects.all().first()
        if obj:
            serializer = self.serializer_class(obj, data=request.data)
        else:
            serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        obj = CustomizedProduct.objects.all().first()
        best_sellers_list = Product.objects.filter(pk__in=obj.best_sellers)
        new_products_list = Product.objects.filter(pk__in=obj.new_products)
        sale_products_list = Product.objects.filter(pk__in=obj.sale_products)
        data = self.serializer_class(obj).data
        data['best_sellers_list'] = ProductSerializer(best_sellers_list, many=True).data
        data['new_products_list'] = ProductSerializer(new_products_list, many=True).data
        data['sale_products_list'] = ProductSerializer(sale_products_list, many=True).data
        return Response(data)
