
#! Django function and methods
from django import forms


#!Models,Forms and Serializer classes
from .models import *


#*BookTitleForm
class BookTitleForm(forms.ModelForm):
    class Meta:
        model = BookTitle
        fields = ('book_title','book_publisher','book_author')