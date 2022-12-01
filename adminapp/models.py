from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from unicodedata import category
from django.db import models
from enum import unique
from django.db import models
from accounts.models import Accounts
#from userapp.models import OrderTable, OrderItem
# Create your models here.
import math
from VEGIE_PROJECT import settings
class Category(models. Model):
    name = models.CharField(max_length = 255 )
    description = models.TextField(blank = True)

    offer = models.IntegerField( default=0)

    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self) :
        return self.name
    
    

class Product(models.Model):
    
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL, null=True)
    name =    models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    image = models.ImageField(null=True, blank=True,max_length = 255000, upload_to ='media/' )
    image2 = models.ImageField(null=True, blank=True,max_length = 255000, upload_to ='media/' )
    image3 = models.ImageField(null=True, blank=True,max_length = 255000, upload_to ='media/' )
    price = models.IntegerField()
    total_quantity = models.IntegerField(default=0)
    instock = models.BooleanField(default=True)
    offer = models.IntegerField( default=0)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
    
    @property
    def get_offer_price(self):
        offer=int(self.offer)
        offer=offer-100
        offer_price = int(self.price) * int(offer)
        offer_price=offer_price/100
        offer_price=offer_price*-1
        return int(offer_price)
    
    @property
    def offer_category_price(self):
        offer = int(self.category.offer)
        offer=100-offer
        offer_price=(int(self.price)*offer)/100
        return int(offer_price)
    
    @property
    def final_price(self):
        if self.offer >= self.category.offer:
            offer=int(self.offer)
            offer=offer-100
            offer_price = int(self.price) * int(offer)
            offer_price=offer_price/100
            offer_price=offer_price*-1
            return int(offer_price)
        elif self.offer <= self.category.offer:
            offer = int(self.category.offer)
            offer=100-offer
            offer_price=(int(self.price)*offer)/100
            return int(offer_price)
        else:
            offer = int(self.category.offer)
            offer=100-offer
            offer_price=(int(self.price)*offer)/100
            return int(self.price)
            
    
    @property
    def product_offer(self):
        pro = self.offer
        return int(pro)
    @property
    def category_offer(self):
        cat = self.category.offer
        return int(cat)
    @property
    def get_image_url(self):
        return'{}{}'.format(settings.CLOUDINARY_URL,self.image)
    @property
    def get_image_url2(self):
        return'{}{}'.format(settings.CLOUDINARY_URL,self.image2)
    @property
    def get_image_url3(self):
        return'{}{}'.format(settings.CLOUDINARY_URL,self.image3)
    @property
    def get_category_name(self):
        cat = self.category.name
        return str(cat)

class Coupen(models.Model):
    coupen_code = models.CharField(max_length=10, default='Default') 
    is_expired = models.BooleanField(default=False)
    discount_price = models.IntegerField(default=100)
    minimum_amount  = models.IntegerField(default=500)
    user            = models.ManyToManyField(Accounts)
    def get_user(self):
        return self.user
    
    
class user_coupon(models.Model):
    coupon = models.ForeignKey(Coupen, on_delete = models.CASCADE)
    user = models.ForeignKey(Accounts, on_delete = models.CASCADE)    
        
