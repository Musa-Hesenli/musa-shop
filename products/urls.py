from django.urls import path
from .views import Products, RelatedImagesView

urlpatterns = [
    path('api/products', Products.as_view(), name='product list'),
    path('api/images', RelatedImagesView.as_view(), name='images')
]