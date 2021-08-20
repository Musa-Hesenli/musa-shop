from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    count = models.IntegerField()
    

class Favorites(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    
class Orders(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    products = models.CharField(max_length=1000)  
    address = models.CharField(max_length=1000, null=True)
