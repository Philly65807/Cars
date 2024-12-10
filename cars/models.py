from django.contrib import admin
from django.db import models
# Create your models here.

class Cars(models.Model):
    name = models.CharField(max_length=100),
    model = models.CharField(max_length=100),
    make = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    year= models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image= models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.make} {self.model}"


from django.contrib.auth.models import User


from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.model} {self.name}"

class Payment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]
    payment_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.payment_id} - {self.status}"

class CarPurchase(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100)
    buyer_email = models.EmailField()
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)


    def __str__(self):
        return f"Purchase of {self.car.name} by {self.buyer_name}"

#


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)



