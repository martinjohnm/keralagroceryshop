from django import forms
from django.forms import ModelForm

from .models import Accounts

# Create a Accounts Form

class AccountForm(ModelForm):
    class Meta:
        model = Accounts
        fields = "__all__"