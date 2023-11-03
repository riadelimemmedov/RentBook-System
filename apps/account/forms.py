
#!Python Modules
import re

#! Django function and methods
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator


#!Helpers Function and Database Modules
from config.helpers import (domain_pattern,body_pattern)


#!Models,Forms and Serializer classes
from .models import Account


#*AccountForm
class AccountForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male'),
        ]
    
    ACCOUNT_TYPE_CHOICES = [
        ('Buyer','Buyer'),
        ('Seller','Seller')
    ]
    
    gender = forms.CharField(widget=forms.TextInput())
    account_type = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = Account
        fields = ['first_name','last_name','gender','account_type','email','phone','password']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if re.match(domain_pattern,email) is None:
            return forms.ValidationError('Enter a valid email address')
        return email        
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name') if self.cleaned_data.get('first_name') is not None else forms.ValidationError('You must provide a first name for this account')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name') if self.cleaned_data.get('last_name') is not None else forms.ValidationError('You must provide a last name for this account')
        return last_name
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone') if self.cleaned_data.get('phone') is not None else forms.ValidationError('You must provide a phoner number for this account')
        return phone