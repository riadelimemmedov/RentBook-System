#

#! Django function and methods
from django.core.management import BaseCommand


#!Models,Forms, and Serializer classses
from apps.author.models import *
from apps.publisher.models import *
from apps.book.models import *
from apps.customer.models import *


#! Third Party Packages
from django_countries.fields import Country


#!Python modules and function
import random



#*Command
class Command(BaseCommand):
    help = "generate dummy data for testing purposes"
    
    def handle(self, *args, **kwargs):
        #generate authors
        authors = ['Andrew Hunt','Martin Kleppmann','Gayle Laakmann','Stanley Chiang','Mark Richards']
        for author in authors:
            author_name,author_surname = author.split()
            Author.objects.create(author_name=author_name,author_surname=author_surname)
            
        
        #generate publishers
        publishers = [
            {'publisher_name':'Addison-Wesley Professional','publisher_country':'us'},
            {'publisher_name':'OReilly Media','publisher_country':'de'},
            {'publisher_name':'CareerCup 6 th edition','publisher_country':'gb'},
            {'publisher_name':'Independently published ','publisher_country':'pl'},
            {'publisher_name':'OReilly Media 1 st edition','publisher_country':'us'}            
        ]
        for publisher in publishers:
            Publisher.objects.create(**publisher)
            
            
        #generate book title
        book_titles = ['Progmatic Programmer','Crack Interview','Data Intensive Application','Hacking the System Design Interview','Software Hard Parts']
        book_publishers = [x.publisher_name for x in Publisher.objects.all()]
        book_titles_items = zip(book_titles,book_publishers)
        
        for item in book_titles_items:
            book_author = Author.objects.order_by('?')[0]
            publisher = Publisher.objects.get(publisher_name=item[1])
            BookTitle.objects.create(book_title=item[0],book_publisher=publisher,book_author=book_author)
        
        
        #generate category book
        category_title = ['System Design','Computer Architecture','Cyber Security','Software Architecture','Design Pattern']
        for category in category_title:
            CategoryBook.objects.create(category_book_name=category)
        
        
        #generate book
        book_book_titles = [x.book_title for x in BookTitle.objects.all()]
        book_language = ['af','eng','fr','de','it']
        book_type = ['book_type','journal_type','cartoon_herous_type']
        book_category = [x.category_book_name for x in CategoryBook.objects.all()]
        book_items = zip(book_book_titles,book_category)
        
        for bookitem in book_items:
            book_t = BookTitle.objects.get(book_title=bookitem[0])
            book_c = CategoryBook.objects.get(category_book_name=bookitem[1])
            selected_book_language = random.choice(book_language)
            selected_book_type = random.choice(book_type)
            Book.objects.create(title=book_t,book_category=book_c,book_language=selected_book_language,book_type=selected_book_type)
            
        
        #generating customers
        customers_list = [
            {'customer_first_name':'John','customer_last_name':'Doe'},
            {'customer_first_name':'Adam','customer_last_name':'Harris'},
            {'customer_first_name':'Lisa','customer_last_name':'Martinez'},
        ]
        
        for customer in customers_list:
            Customer.objects.create(**customer)


