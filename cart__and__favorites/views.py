from django.db.models import fields
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from .models import Cart, Favorites, Orders
from rest_framework.response import Response
from rest_framework import status

from products.serializers import ProductSerializer
# Create your views here.

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartView(APIView):
    def get(self, request, user_id):
        cart__items = Cart.objects.filter(user_id = user_id)
        serializer = CartSerializer(cart__items, many = True)
        return Response(serializer.data)

    def post(self, request, user_id = None):
        print(request.data)
        cart_item = Cart.objects.filter(user_id = request.data['user_id'], product_id = request.data['product'])
        if len(cart_item) != 0:
            return Response({'message' : 'This item is already exists'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = CartSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, user_id = None):
        cart_item = Cart.objects.filter(user_id = user_id, product = request.data['product_id'])
        if cart_item is not None:
            cart_item.delete()
            return Response(data = cart_item,status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)    
            
        
class FavoritesSerializer(ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'


class FavoritesView(APIView):
    def get(self, request):
        user_id = request.GET['user_id']
        products = Favorites.objects.filter(user_id = user_id)
        serializer = FavoritesSerializer(products, many = True)
        return Response(serializer.data)

    def post(self, request):
        print('Request data: ',request.data)
        favorite_item = Favorites.objects.filter(user_id = request.data['user_id'], product = request.data['product'])
        if len(favorite_item) != 0:
            print(favorite_item)
            return Response({'message' : 'This item is already exists'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = FavoritesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request):
        user_id = request.data['user_id']
        product = request.data['product']
        favorite_item = Favorites.objects.filter(user_id = user_id, product = product)
        if favorite_item is not None:
            favorite_item.delete()
            return Response(product,status = status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)           


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'



class OrderView(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        cart_item = Cart.objects.filter(user_id = user_id)
        cart_item.delete()
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)    