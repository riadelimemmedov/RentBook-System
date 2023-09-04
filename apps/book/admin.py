
#! Django function and methods
from django.contrib import admin
from django.core.exceptions import ValidationError


#!Models,forms and serializer classes
from .models import *

# Register your models here.



#*BookTitleModelAdmin
class BookTitleModelAdmin(admin.ModelAdmin):
    list_display = ['book_title','book_slug','book_publisher','book_author','created','modified']
    list_display_links = ['book_title','book_slug']
    
    
#register created custokm model to django admin site
admin.site.register(BookTitle,BookTitleModelAdmin)



#*BookModelAdmin
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title','book_id','qr_code','created','modified']
    list_display_links = ['title','qr_code']
    
    
#register created custokm model to django admin site
admin.site.register(Book,BookModelAdmin)