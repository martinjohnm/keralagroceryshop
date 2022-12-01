from ast import Try
from email.policy import default
from operator import mod
from pyexpat import model
from random import choices
from tokenize import blank_re
from django.db import models
from django.forms import IntegerField
from adminapp.models import Category, Product,Coupen
from accounts.models import Accounts
from adminapp.models import Coupen
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True,)
    session_id = models.CharField(max_length = 100, null=True)
    coupon = models.ForeignKey(Coupen, on_delete=models.SET_NULL, null=True,blank=True )
    
    def get_cart_total(self):
        product = self.product
        quantity = self.product
        price = self.product.final_price
        return price*quantity
        
    def get_coupon_code(self):
        return None    


class Address(models.Model):
    user            = models.ForeignKey(Accounts,on_delete=models.CASCADE,null = True)
    name       = models.CharField(max_length=200,null = True)
    phone_number    = models.CharField(max_length=99,null = True)
    house_name      = models.CharField(max_length=200, null = True)
    street_name      = models.CharField(max_length=200, null = True)
    landmark      = models.CharField(max_length=200, null = True)
    city            = models.CharField(max_length=200, null = True)
    default_address         = models.BooleanField(default=False)
    pin_code       = models.IntegerField( null = True)
    
class OrderTable(models.Model):
         
    COD = 'COD' 
    RAZORPAY = 'RAZORPAY'
    PAYPAL = 'PAYPAL'
    
    PAYMENT_METHOD=[
   
        
        (COD, 'Cash On Delivery'),
        (RAZORPAY, 'Razor Pay'),
        (PAYPAL, 'Paypal')
    ]

    user            = models.ForeignKey(Accounts,on_delete= models.CASCADE, null = True ,blank = True )
    amount          = models.FloatField(default=0)
    is_paid         = models.BooleanField(default=False)
    order_id        = models.CharField(max_length = 100, blank=True)
    payment_method  = models.CharField(max_length=100,choices = PAYMENT_METHOD, default=COD)
    payment_id      = models.CharField(max_length=100, blank=True)

    name            = models.CharField(max_length=100, blank=True)
    phone_number    = models.CharField(max_length=100, blank=True)
    house_name      = models.CharField(max_length=100, blank=True)
    street_name     = models.CharField(max_length=100, blank=True)
    landamrk        = models.CharField(max_length=100, blank=True)
    city            = models.CharField(max_length=100, blank=True)
    pincode         = models.CharField(max_length=100, blank=True)
    orderstatus = [
        ('Pending', 'Pending'),
        ("Confirmed", 'Confirmed'),
        ("Delivered", "Delivered"),
        ('Completed', 'Completed'),
        ('Rejected', 'Rejected'),
        ('Canceled', 'Canceled'),
        ('Returned', 'Returned'),
    ]
    status          = models.CharField(max_length=100, choices = orderstatus, default='Pending')
    message         = models.TextField(null = True)
    created_at      = models.DateTimeField(auto_now_add=True)
    tracking_no     = models.CharField(max_length=100, default='none')
    date_delivered  = models.DateField(auto_now_add= False,default='2022-01-01')

    coupon          = models.ForeignKey(Coupen,on_delete= models.CASCADE, null = True ,blank = True)


class OrderItem(models.Model):
    order           = models.ForeignKey(OrderTable, on_delete=models.CASCADE)    
    product_name    = models.CharField(max_length=100, blank=True)
    product         = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price           = models.IntegerField(null=False)
    quantity        = models.IntegerField(null=False)
    
 