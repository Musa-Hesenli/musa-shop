from django.urls import path
from .views import UserAccountView, MyTokenObtainPairView

urlpatterns = [
    path('create-account', UserAccountView.as_view(), name = 'Register'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', MyTokenObtainPairView.as_view(), name='token_refresh'),
]