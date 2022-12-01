from email.policy import default
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,BaseUserManager)


# Create your models here.

class AccountManger(BaseUserManager):
    def _create_user(self, first_name, last_name, username, email, phone, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not username:
            raise ValueError('The given email must be set')
        if not email:
            raise ValueError('The given email must be set')
        user = self.model(
            first_name      = first_name,
            last_name       = last_name,
            username        = username,
            email           = email,
            phone           = phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, last_name, username, email, phone, password, **extra_fields):
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(first_name, last_name, username, email, phone, password, **extra_fields)

    def create_superuser(self, first_name, last_name, username, email, phone, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(first_name, last_name, username, email, phone, password, **extra_fields)




    
    

    

class Accounts(AbstractBaseUser,PermissionsMixin):
    first_name              = models.CharField(max_length=50, null=True)
    last_name               = models.CharField(max_length=50, null=True)
    username                = models.CharField(max_length=50, unique=True)
    email                   = models.CharField(max_length=50, unique=True)
    phone                   = models.CharField(max_length=40, unique=True)


    #required fields

    date_joined             = models.DateTimeField(auto_now_add=True)
    last_login              = models.DateTimeField(auto_now_add=True)
    is_admin                = models.BooleanField(default=False)
    is_staff                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_superuser            = models.BooleanField(default=False)
    
    
    

    def __str__(self):
        return self.username

    objects                  = AccountManger()
    USERNAME_FIELD              = 'email'
    REQUIRED_FIELDS         = ['first_name', 'last_name', 'phone', 'username']

    class Meta:
        verbose_name        = 'Account'
        verbose_name_plural = 'Accounts'

class CustomerAdress(models.Model):
    user                    = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)
    first_name              = models.CharField(max_length=200)
    last_name               = models.CharField(max_length=200)
    email                   = models.EmailField(max_length=254)
    phone_number            = models.CharField(max_length=99)
    house_name              = models.CharField(max_length=200, null=True)
    street_name             = models.CharField(max_length=200, null=True)
    city                    = models.CharField(max_length=200, null=True)
    state                   = models.CharField(max_length=200, null=True)
    country                 = models.CharField(max_length=200, null=True)
    post_code               = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user)

        
    

class Wallet(models.Model):
    
    Balance                 = models.IntegerField(default=0)
    
    user                    = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)


class WalletTransactions(models.Model):
    wallet                  = models.ForeignKey(Wallet, on_delete=models.CASCADE, null=True ) 
    amount                  = models.IntegerField(default=0)    
    user                    = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)
    CREDIT = 'CREDIT' 
    DEBIT = 'DEBIT'
    
    
    
    
    PAYMENT_METHOD=[
   
        
        (CREDIT, 'CREDIT'),
        (DEBIT, 'DEBIT'),
        
    ]
    
    status                  = models.CharField(max_length=100,choices = PAYMENT_METHOD, null=True)
    
