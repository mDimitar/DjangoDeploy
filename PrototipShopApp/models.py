from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sale = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    image = models.URLField()

    def __str__(self):
        return self.name + " " + self.description + " " + self.category.name + " " + self.brand.name + " " + self.type.name

class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    products = models.ManyToManyField(Product,blank=True)
    def __str__(self):
        return "Shopping Cart for " + str(self.user)

