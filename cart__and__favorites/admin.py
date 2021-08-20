from django.contrib import admin
from .models import Cart, Favorites, Orders

# Register your models here.
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Favorites)