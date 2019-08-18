from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class SalesRep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commission_percent = models.DecimalField(decimal_places=2, max_digits=3)
    commission_total = models.DecimalField(default=0, blank=True, decimal_places=2, max_digits=99)
    commission_to_date = models.DecimalField(default=0, blank=True, decimal_places=2, max_digits=99)
    total_sales = models.DecimalField(default=0, blank=True, decimal_places=2, max_digits=99)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " | "  + self.user.username


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    store_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=1000)
    amount_spent = models.DecimalField(default=0, blank=True, max_digits=99, decimal_places=2)

    def __str__(self):
        return self.name + " | " + self.store_name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=99, decimal_places=2)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class ProductList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.product + " x " + self.amount


class Order(models.Model):
    products = models.ManyToManyField(ProductList)
    salesrep = models.ForeignKey(SalesRep, blank=True, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date_ordered = models.DateField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return "Order number #{} for {} from {}".format(self.pk, self.salesrep, self.customer)
