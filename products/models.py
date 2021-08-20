from django.db import models

COLOR_CHOICES = [
    ('black', '#000'),
    ('green', 'green'),
    ('indigo', 'indigo'),
    ('yellow', 'yellow'),
    ('mediumseagreen', 'Medium Sea Green'),
]
# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField(max_length = 30)
    slug = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Product Categories'    

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length = 500)
    color = models.CharField(choices=COLOR_CHOICES, max_length=100)
    image = models.ImageField(null = True, upload_to = 'products/front')
    views = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    sex = models.CharField(choices=[('women', "Women"),('man', 'Man'), ('Children', "Children") ], max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Products'    

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()

    class Meta:
        verbose_name_plural = "Images"

class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        verbose_name_plural = "Reviews"



