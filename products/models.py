from typing import Any
from django.db import models

# Create your models here.
# models = таблица!!!
class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    quantity = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'

# class Sum:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

# sum = Sum(1,2)
# total = sum.a * sum.b
