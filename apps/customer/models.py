
#! Django function and methods
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify



#! Third Party Packages
from django_extensions.db.fields import AutoSlugField,RandomCharField
from django_extensions.db.models import TimeStampedModel




#!Helpers methods and functions
from config.helpers import (setFullName)


# Create your models here.


#*Customer
class Customer(TimeStampedModel):
    customer_first_name = models.CharField(_('First Name'), max_length=100)
    customer_last_name = models.CharField(_('Last Name'), max_length=100)
    customer_username = models.CharField(_('Username'), max_length=100,blank=True,null=True,unique=True)
    customer_slug = AutoSlugField(_('Slug'), populate_from='customer_username',unique=True,blank=True,null=True)
    customer_additional_information = models.TextField(_('Additional Information'),blank=True)
    customer_rating = models.PositiveSmallIntegerField(_('Rating'), default=50)
    customer_key = RandomCharField(_('Customer Id'),length=24,unique=True,blank=True,include_alpha=True)
    
    customer_books = models.ManyToManyField("book.Book",blank=True,help_text='Books that are currently rented')
    customer_book_count = models.PositiveSmallIntegerField(_('Book Count'),default=0)
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        
    
    def __str__(self):
        return f"{self.customer_first_name} - {self.customer_last_name}"
    
    
    def save(self, *args, **kwargs):
        if not self.customer_username:
            username = setFullName(self.customer_first_name,self.customer_last_name)
            ex = __class__.objects.filter(customer_username=username).exists()
            while ex:
                i = len(__class__.objects.filter(customer_first_name=self.customer_first_name,customer_last_name=self.customer_last_name))
                username = f"{self.customer_first_name} {self.customer_last_name}{i+1}"
                ex = __class__.objects.filter(customer_username=username).exists()#If return false,break out while loop and save username to database
            self.customer_username = username
        super(Customer, self).save(*args, **kwargs)
    
    
    