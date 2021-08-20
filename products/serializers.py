from django.db.models import fields
from rest_framework import serializers
from .models import Product, Images

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'        