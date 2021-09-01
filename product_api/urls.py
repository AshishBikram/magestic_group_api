from django.urls import path
from .views import ProductCLView, ProductPGDView, ProductImageCLView, ProductImagePGDView, ProductCategoryCLView, \
    ProductCategoryPGDView

urlpatterns = [
    path('product', ProductCLView.as_view()),
    path('product/<int:pk>', ProductPGDView.as_view()),
    path('product-image', ProductImageCLView.as_view()),
    path('product-image/<str:pk>', ProductImagePGDView.as_view()),
    path('product-category', ProductCategoryCLView.as_view()),
    path('product-category/<int:pk>', ProductCategoryPGDView.as_view()),
]