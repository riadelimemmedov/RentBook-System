
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



#!Models,Forms and Serializer classes
from apps.rental.choices import *


#!Python modules and function
import uuid
from io import BytesIO
from PIL import Image



# Create your models here.



#*TagBook
class TagBook(TimeStampedModel):
    tag_book_name = models.CharField(_('Name'), max_length=50, blank=False,unique=True,db_index=True,help_text='Enter book tag')
    tag_book_slug = AutoSlugField(_('Slug'),populate_from='tag_book_name',unique=True,db_index=True,blank=True)
    
    
    class Meta:
        verbose_name = 'Tag Book'
        verbose_name_plural = 'Tags Book'
        
        
    def __str__(self):
        return f"{self.tag_book_name}"
    
    
    def tag_count(self):
        return self.tag_book.all().count()




#*CategoryBook
class CategoryBook(TimeStampedModel):
    category_book_name = models.CharField(_('Name'),max_length=50,blank=False,unique=True,db_index=True,help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    category_book_slug = AutoSlugField(_('Slug'),populate_from='category_book_name',unique=True,db_index=True,blank=True)

    class Meta:
        verbose_name = 'Category Book'
        verbose_name_plural = 'Categoryies Book'
        

    def __str__(self):
        return f"{self.category_book_name}"
    
    
    def category_count(self):
        return self.category_book.all().count()
    
    


#*BookTitle
class BookTitle(TimeStampedModel):
    book_title = models.CharField(_('Title'),max_length=200,unique=True)
    book_slug = AutoSlugField(_('Slug'),populate_from='book_title',db_index=True,unique=True,blank=True,null=True)
    book_publisher = models.ForeignKey("publisher.Publisher",verbose_name=(_('Publisher')),on_delete=models.CASCADE)
    book_author = models.ForeignKey("author.Author",verbose_name=(_('Author')),on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = 'Book Title'
        verbose_name_plural = 'Books Title'
        
    def __str__(self):
        return f"Book position : {self.book_title}"
    
    
    @property
    def books(self):
        return self.booktitle.all()

#*Book
class Book(TimeStampedModel):
    class BookChoices(models.TextChoices):
        BOOK = "book_type",_("Book Type")
        JOURNAL = "journal_type",_("Journal Type")
        CartoonHerous = "cartoon_herous_type",_("Cartoon Hereous Type")
        
    class LanguagesChoices(models.TextChoices):
        AFRICA = 'af',_('Afrikaans')
        ALBANIAN = 'sq',_('Albanian')
        AMHARIC = 'am',_('Amharic')
        ARABIC = 'ar',_('Arabic')
        AZERBAIJANI = 'az',_('Azerbaijani')
        BASQUE = 'eu',_('Basque')
        BELARUSIAN = 'be',_('Belarusian')
        BENGALI = 'bn',_('Bengali')
        BOSNIAN = 'bs',_('Bosnian')
        BULGARIAN = 'bg',_('Bulgarian')
        CATALAN = 'ca',_('Catalan')
        CEBUANO = 'ceb',_('Cebuano')
        CHICHEWA = 'ny',_('Chichewa')
        CORSICAN = 'co',_('Corsican')
        CROATIAN = 'hr',_('Croatian')
        CZECH = 'cs',_('Czech')
        DANISH = 'da',_('Danish')
        DUTCH = 'nl',_('Dutch')
        ENGLISH = 'eng',_('English')
        ESPERANTO = 'eo',_('Esperanto')
        ESTONIAN = 'et',_('Estonian')
        FILIPINO = 'tl',_('Filipino')
        FINNISH = 'fi',_('Finnish')
        FRENCH = 'fr',_('French')
        FRISIAN = 'fy',_('Frisian')
        GALICIAN = 'gl',_('Galician')
        GEORGIAN = 'ka',_('Georgian')
        GERMAN = 'de',_('German')
        GREEK = 'el',_('Greek')
        GUJARATI = 'gu',_('Gujarati')
        HINDI = 'hi',_('Hindi')
        HUNGARIAN = 'hu',_('Hungarian')
        INDONESIAN = 'id',_('Indonesian')
        IRISH = 'ga',_('Irish')
        ITALIAN = 'it',_('Italian')
        JAPANESE = 'ja',_('Japanese')
        CANADA = 'kn',_('Canada')
        KAZAKH = 'kk',_('Kazakh')
        KOREAN = 'ko',_('Korean')
        LATIN = 'la',_('Latin')
        LATVIAN = 'lv',_('Latvian')
        MACEDONIAN = 'mk',_('Macedonian')
        PORTUGUESE = 'pt',_('Portuguese')
        ROMANIAN = 'ro',_('Romanian')
        RUSSIAN = 'ru',_('Russian')
        SPANISH = 'es',_('Spanish')
        SWEDISH = 'sv',_('Swedish')
        TURKISH = 'tr',_('Turkish')
        UKRAINIAN = 'uk',_('Ukrainian')
        UZBEK = 'uz',_('Uzbek')
        VIETNAMESE = 'vi',_('Vietnamese')
        WELSH = 'cy',_('Welsh')

    
    title = models.ForeignKey(BookTitle,verbose_name=(_('Book Title')),on_delete=models.CASCADE,related_name='booktitle')
    book_isbn = RandomCharField(_('Book Id'),length=13,unique=True,blank=True,include_alpha=True,null=True)
    qr_code = models.ImageField(_('Qr Code'),upload_to='qr_codes',blank=True,null=True,validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    book_language = models.CharField(_('Language'),max_length=50,choices=LanguagesChoices.choices,null=True)
    book_summary=models.TextField(_('Summary'),max_length=800,null=True,blank=True,help_text="Summary about the book")
    book_pages = models.PositiveIntegerField(_('Pages Count'),default=0)
    book_category = models.ForeignKey(CategoryBook,verbose_name=(_('Category Book')),on_delete=models.SET_NULL,null=True,related_name='category_book')
    book_tag = models.ManyToManyField(TagBook,verbose_name=(_('Tag Book')),null=True, related_name='tag_book')
    book_type = models.CharField(_('Type'),max_length=50,choices=BookChoices.choices,null=True)
    in_stock = models.BooleanField(_('In Stock'),default=False)
    edition = models.IntegerField(_('Edition'),blank=True,null=True)
    published_date = models.DateField(_('Published Date'),blank=True,null=True)
    available_copies = models.IntegerField(_('Available Copies'),default=0)
    
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    
    def __str__(self):
        return f"{self.title} - {self.book_language}"
    
    
    @property
    def status(self):
        if len(self.rental_set.all()) > 0:
            statuses = dict(STATUS_CHOICES)
            if len(self.rental_set.all()) > 1:
                for rentalbook in self.rental_set.all():
                    return rentalbook
            else:
                return statuses[self.rental_set.all().first().rented_status]
        return False
    
    def save(self,*args,**kwargs):
        #generate qr code 
        qrcode_img = qrcode.make(self.book_isbn)
        canvas = Image.new('RGB',(qrcode_img.pixel_size,qrcode_img.pixel_size),'white')
        canvas.paste(qrcode_img)
        fname = f"qr_codes-{self.book_isbn}.png"
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        super(Book, self).save(*args,**kwargs)