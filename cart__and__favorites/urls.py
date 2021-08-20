from django.urls import path
from .views import CartView, FavoritesView, OrderView

urlpatterns = [
    path('cart/<str:user_id>', CartView.as_view(), name='cart'),
    path('favorites', FavoritesView.as_view(), name='favorites'),
    path('orders', OrderView.as_view(), name='order')
]