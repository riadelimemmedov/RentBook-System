
#! Django function and methods
from django import forms


#!Models,Forms and Serializer classes
from .models import *


#*BookTitleForm
class BookTitleForm(forms.ModelForm):
    class Meta:
        model = BookTitle
        fields = ('book_title','book_publisher','book_author')
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'border bg-purple-200 rounded-xl p-3'}),
        #     'author': forms.Select(attrs={'class': 'border bg-purple-200 rounded-xl p-3'}),
        #     'publisher': forms.Select(attrs={'class': 'border bg-purple-200 rounded-xl p-3'})
        # }
    
    def clean(self):
        book_title = self.cleaned_data.get('book_title')
                
        if(len(book_title)<5):
            error_msg = 'The title is too short'
            self.add_error('book_title',error_msg)
            
        book_title_exists = BookTitle.objects.filter(book_title__iexact=book_title).exists()
        if book_title_exists:
            self.add_error('book_title','This book title already exists')
        
        return self.cleaned_data