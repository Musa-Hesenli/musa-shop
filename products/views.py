from django.db.models.base import Model
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Images, Product
from .serializers import ImageListSerializer, ProductSerializer
from rest_framework import status
# Create your views here.

class Products(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class RelatedImagesView(APIView):
    def get(self, request):
        product_id = request.GET['product_id']
        images = Images.objects.filter(product = product_id)
        serializer = ImageListSerializer(images, many = True)
        return Response(serializer.data)             