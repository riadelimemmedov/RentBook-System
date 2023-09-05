
#! Django function and methods
from django.contrib import admin
from django.core.exceptions import ValidationError


#!Models,forms and serializer classes
from .models import *


# Register your models here.


#* PublisherModelAdmin
class PublisherModelAdmin(admin.ModelAdmin):
    list_display = ['id','publisher_name','publisher_country','created','modified','publisher_id']
    list_display_links = ['id','publisher_name','publisher_country']
    
    
#register created custokm model to django admin site
admin.site.register(Publisher,PublisherModelAdmin)