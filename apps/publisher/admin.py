
#! Django function and methods
from django.contrib import admin
from django.core.exceptions import ValidationError


#!Models,forms and serializer classes
from .models import *


#! Third Party Packages
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

# Register your models here.




#?PublisherResource
class PublisherResource(resources.ModelResource):
    created = Field()
    modified = Field()
    
    class Meta:
        model = Publisher
        fields = ['id','publisher_name','publisher_country','created','modified','publisher_id']
        export_order = fields

    
    def dehydrate_created(self,obj):
        return obj.created.strftime("%d/%m/%y")


    def dehydrate_modified(self,obj):
        return obj.modified.strftime("%d/%m/%y")


#* PublisherModelAdmin
class PublisherModelAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ['id','publisher_name','publisher_country','created','modified','publisher_id']
    list_display_links = ['id','publisher_name','publisher_country']
    resource_class = PublisherResource
    
#register created custokm model to django admin site
admin.site.register(Publisher,PublisherModelAdmin)