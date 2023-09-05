
#! Django function and methods
from django.contrib import admin


#!Models,forms and serializer classes
from .models import *

# Register your models here.



#*CustomerModelAdmin
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['customer_first_name','customer_last_name','customer_key','customer_rating','customer_book_count','customer_slug']
    list_display_links = ['customer_first_name','customer_last_name']
    
    
#register created custokm model to django admin site
admin.site.register(Customer,CustomerModelAdmin)

