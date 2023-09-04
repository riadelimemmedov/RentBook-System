
#! Django function and methods
from django.db import models
from django.utils.translation import gettext_lazy as _



#! Third Party Packages
from django_extensions.db.models import TimeStampedModel
from django_countries.fields import CountryField



#!Python modules and function
import uuid

# Create your models here.


#*Publisher
class Publisher(TimeStampedModel):
    """Book publisher Managed only in the django admin"""
    id = models.UUIDField(_('Id'),primary_key=True,default=uuid.uuid4(),editable=False)
    publisher_name = models.CharField(_('Name'),max_length=200)
    publisher_country = CountryField(blank_label=('select country'))
    
    
    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'
        
    def __str__(self):
        return f"{self.publisher_name} from {self.publisher_country}"
    
    
    