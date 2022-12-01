from dataclasses import fields
from django.forms import ModelForm
from .models import Address


class CustomerForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'