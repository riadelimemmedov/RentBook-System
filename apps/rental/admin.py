
#! Django function and methods
from django.contrib import admin


#!Models,forms and serializer classes
from .models import *


# Register your models here.


#* RentalModelAdmin
class RentalModelAdmin(admin.ModelAdmin):
    list_display = ['rented_book','rented_customer','rented_status','rental_id','rent_start_date','rent_end_date','return_date','is_closed']
    list_display_links = ['rented_book','rented_customer','rented_status']
    
    
#register created custokm model to django admin site
admin.site.register(Rental,RentalModelAdmin)