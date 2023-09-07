
#! Django function and methods
from django.contrib import admin
from django.core.exceptions import ValidationError


#!Third party application
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field


#!Models,forms and serializer classes
from .models import *
from apps.rental.choices import *


# Register your models here.



#?BookResource
class BookResource(resources.ModelResource):
    title = Field()
    status = Field()
    book_publisher = Field()
    class Meta:
        model = Book
        fields = ['title','book_isbn','qr_code','book_author','created','modified','status','book_publisher']
        

    def dehydrate_title(self, obj):
        return obj.title.book_title
    
    def dehydrate_book_publisher(self, obj):
        return obj.title.book_publisher.publisher_name
    
    def dehydrate_status(self, obj):
        statuses = dict(STATUS_CHOICES)
        rented_books = [{x.rented_customer.customer_username:statuses[x.rented_status]} for x in obj.rental_set.all()]
        return rented_books


#*BookTitleModelAdmin
class BookTitleModelAdmin(admin.ModelAdmin):
    list_display = ['book_title','book_slug','book_publisher','book_author','created','modified']
    list_display_links = ['book_title','book_slug']
    
    
#register created custokm model to django admin site
admin.site.register(BookTitle,BookTitleModelAdmin)



#*BookModelAdmin
class BookModelAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ['title','book_isbn','qr_code','created','modified']
    list_display_links = ['title','qr_code']
    resource_class = BookResource
    
    
#register created custokm model to django admin site
admin.site.register(Book,BookModelAdmin)


admin.site.register(CategoryBook)