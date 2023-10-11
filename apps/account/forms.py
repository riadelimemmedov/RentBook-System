
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
    def clean_email(self):
        print('Worked clean email')
        email = self.cleaned_data.get('email')
        if re.match(domain_pattern,email) is None:
            return forms.ValidationError('Enter a valid email address')
        return email        
    
    def clean_first_name(self):
        print('Worked clean first name')
        first_name = first_name if self.cleaned_data.get('first_name') is not None else forms.ValidationError('You must provide a first name for this account')
        return first_name
    
    def clean_last_name(self):
        print('Worked clean last name')
        last_name = last_name if self.cleaned_data.get('last_name') is not None else forms.ValidationError('You must provide a last name for this account')
        return last_name