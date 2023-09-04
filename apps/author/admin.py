
#! Django function and methods
from django.contrib import admin
from django.core.exceptions import ValidationError


#!Models,forms and serializer classes
from .models import *
from .forms import AuthorForm

# Register your models here.



#*AuthorModelAdmin
class AuthorModelAdmin(admin.ModelAdmin):
    form = AuthorForm
    list_display = ['author_name','author_surname','author_fullname','author_email','author_slug','birth_date','died_date']
    list_display_links = ['author_name','author_slug']
    
    
#register created custokm model to django admin site
admin.site.register(Author,AuthorModelAdmin)