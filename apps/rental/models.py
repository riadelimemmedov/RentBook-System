
#! Django function and methods
from django.db import models
from django.utils.translation import gettext_lazy as _



#! Third Party Packages
from django_extensions.db.fields import AutoSlugField,RandomCharField
from django_extensions.db.models import TimeStampedModel



#!Python modules and function
from datetime import timedelta

# Create your models here.


#*Rental
class Rental(TimeStampedModel):
    class RentalStatusChoices(models.TextChoices):
        RENTED = "#0",_("Rented")
        RETURNED = '#1',_("Returned")
        LOST = '#2',_("Lost")
        DELAYED = '#3',_("Delayed")
        
    
    rented_book = models.ForeignKey('book.Book',verbose_name=(_('Book')),on_delete=models.CASCADE)
    rented_customer = models.ForeignKey('customer.Customer',verbose_name=(_('Customer')),on_delete=models.CASCADE)
    rented_status = models.CharField(_('Status'),max_length=20,choices=RentalStatusChoices.choices)
    rental_id = RandomCharField(_('Rental Id'),length=24,unique=True,blank=True,include_alpha=True)
    rent_start_date = models.DateField(help_text=_('When the book was rented'))
    rent_end_date = models.DateField(help_text=_('Deadline return borrowed books'),blank=True)
    return_date = models.DateField(help_text=_('Actual return date,user returned date'),blank=True,null=True)
    is_closed = models.BooleanField(_('Closed'),default=False)#Only True,if rental return or lost
    
    
    class Meta:
        verbose_name = 'Rental Book'
        verbose_name_plural = 'Rental Books'
        ordering = ['-created']
        
    def __str__(self):
        return f"{self.rented_book.book_isbn} rented by {self.rented_customer.customer_username}"
    
    
    def save(self,*args,**kwargs):
        if not self.rent_end_date:
            self.rent_end_date = self.rent_start_date + timedelta(days=14)
        super(Rental, self).save(*args,**kwargs)
        