from django.contrib import admin
from .models import Cars

admin.site.register(Cars)

# Register your models here.
from django.contrib import admin
from .models import Car, CarPurchase, Payment

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'price')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'status', 'amount', 'date')

@admin.register(CarPurchase)
class CarPurchaseAdmin(admin.ModelAdmin):
    list_display = ('car', 'buyer_name', 'buyer_email', 'payment')
