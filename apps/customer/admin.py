
#! Django function and methods
from django.contrib import admin


#!Models,forms and serializer classes
from .models import *



#! Third Party Packages
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

# Register your models here.



#?CustomerResource
class CustomerResource(resources.ModelResource):
    customer_additional_information = Field()
    customer_books = Field()
    class Meta:
        model = Customer
        fields = ['profile','customer_rating','customer_book_count','customer_books','customer_book_count']
        export_order = fields
        
    
    def dehydrate_customer_additional_information(self,obj):
        if not obj.customer_additional_information:
            return "-"
        elif len(obj.customer_additional_information) < 5:
            return obj.customer_additional_information
        else:
            txt_list = obj.customer_additional_information.split(' ')[:5]
            return " ".join(txt_list) + "..."

    
    def dehydrate_customer_books(self,obj):
        books = [book.book_isbn for book in obj.customer_books.all()]
        return ", ".join(books)

#*CustomerModelAdmin
class CustomerModelAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ['profile','customer_rating','customer_book_count','customer_book_count']
    list_display_links = ['profile']
    resource_class = CustomerResource
    
#register created custokm model to django admin site
admin.site.register(Customer,CustomerModelAdmin)

