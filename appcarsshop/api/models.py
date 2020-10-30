from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()

class Order(models.Model):
    direccion = models.CharField(max_length=128)
    date = models.DateTimeField()

class ProductOrdered(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
