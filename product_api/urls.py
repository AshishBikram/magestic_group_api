from django.urls import path
from .views import ProductCLView, ProductPGDView, ProductImageCLView, ProductImagePGDView, ProductCategoryCLView, \
    ProductCategoryPGDView, CustomizedProductCLView, ContactUSCLView, ContactUSPGDView

urlpatterns = [
    path('product', ProductCLView.as_view()),
    path('product/<int:pk>', ProductPGDView.as_view()),
    path('product-image', ProductImageCLView.as_view()),
    path('product-image/<str:pk>', ProductImagePGDView.as_view()),
    path('product-category', ProductCategoryCLView.as_view()),
    path('product-category/<int:pk>', ProductCategoryPGDView.as_view()),
    path('custom-product', CustomizedProductCLView.as_view()),
    path('contact-us', ContactUSCLView.as_view()),
    path('contact-us/<int:pk>', ContactUSPGDView.as_view()),
]