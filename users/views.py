from django.shortcuts import render
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
# Create your views here.

class UserAccountView(APIView):
    def post(self, request):
        print("Username: ",request.data['username'])
        username = request.data['username']
        email = request.data['email']
        if not username or not email:
            return Response({ 'detail' : 'username and email are required field' })

        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            user = 0  
        if user:
            return Response({
                'message' : 'This username is already taken, please try another one',
                'details' : 'User should enter another username'
            }, status = status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email = email)
        except User.DoesNotExist:
            user = 0    
        if user:
            return Response({
                'message' : 'This email is already taken, please try another one',
                'details' : 'User should enter another email'
            }, status = status.HTTP_400_BAD_REQUEST)
            
        serializer = UserSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            user_info = serializer.save()
            user_info.set_password(request.data['password'])
            user_info.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response({ 'details' : 'Someting went wrong', 'message' : 'Try another time' },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['user_id'] = self.user.id
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer