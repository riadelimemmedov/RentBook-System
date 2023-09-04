
#! Django function and methods
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _



#! Third Party Packages
from django_extensions.db.fields import AutoSlugField,RandomCharField
from django_extensions.db.models import TimeStampedModel
from ckeditor.fields import RichTextField


# Create your models here.



#*Author
class Author(TimeStampedModel):
    author_id = RandomCharField(_('Id'),length = 15, unique=True,include_alpha=False)
    author_name = models.CharField(_('Name'),max_length=50,db_index=True,unique=True)
    author_surname = models.CharField(_('Surname'),max_length=50)
    author_fullname = models.CharField(_('Full Name'),max_length=50,null=True,blank=True)
    author_email = models.EmailField(_('Email'),max_length=100,null=True,blank=True)
    author_slug = AutoSlugField(_('Slug'),populate_from='author_fullname',unique=True,blank=True,null=True)
    author_description = RichTextField(_('description'),blank=True,null=True)
    # author_books = 
    birth_date = models.DateField(_("birthdate"),null=True,blank=True)
    died_date  =  models.DateField(_("died_date"),null=True,blank=True)
    
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        
    
    def __str__(self):
        return f"{self.author_name}-{self.author_surname}-{self.author_slug}"
    
    
    def checkAuthorEmailIsExist(self):
        if self.died_date != None:
            self.author_email = ''
        return self.author_email
    
    
    def setAuthorFullName(self):
        self.author_fullname = f"{self.author_name} {self.author_surname}"
        return self.author_fullname
    
    
    def save(self,*args,**kwargs):
        fullName = self.setAuthorFullName()
        isEmailExists = self.checkAuthorEmailIsExist()
        super(Author,self).save(*args,**kwargs)
    
    
    
    