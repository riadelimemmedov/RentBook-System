
#! Django function and methods
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.core.files import File



#! Third Party Packages
from django_extensions.db.fields import AutoSlugField,RandomCharField
from django_extensions.db.models import TimeStampedModel
from django_countries.fields import CountryField
import qrcode



#!Python modules and function
import uuid
from io import BytesIO
from PIL import Image



# Create your models here.


#*BookTitle
class BookTitle(TimeStampedModel):
    book_title = models.CharField(_('Title'),max_length=200,unique=True)
    book_slug = AutoSlugField(_('Slug'),populate_from='book_title',unique=True,blank=True,null=True)
    book_publisher = models.ForeignKey("publisher.Publisher",verbose_name=(_('Publisher')),on_delete=models.CASCADE)
    book_author = models.ForeignKey("author.Author",verbose_name=(_('Author')),on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = 'Book Title'
        verbose_name_plural = 'Books Title'
        
    def __str__(self):
        return f"Book position : {self.book_title}"
    
    

#*Book
class Book(TimeStampedModel):
    title = models.ForeignKey(BookTitle,verbose_name=(_('Book Title')),on_delete=models.CASCADE)
    book_id = RandomCharField(_('Book Id'),length=24,unique=True,blank=True,include_alpha=True)
    qr_code = models.ImageField(_('Qr Code'),upload_to='qr_codes',blank=True,null=True,validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        
    
    def __str__(self):
        return f"{self.title}"
    
    
    def save(self,*args,**kwargs):
        #generate qr code 
        qrcode_img = qrcode.make(self.book_id)
        canvas = Image.new('RGB',(qrcode_img.pixel_size,qrcode_img.pixel_size),'white')
        canvas.paste(qrcode_img)
        fname = f"qr_codes-{self.title}.png"
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        
        super(Book, self).save(*args,**kwargs)