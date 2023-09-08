
#! Django function and methods
from django.shortcuts import render
from django.views.generic import ListView


#!Models,Forms and Serializer classes
from .models import Book,BookTitle


# Create your views here.



#?BookTitleListView
class BookListView(ListView):
    model = Book
    template_name = "book/book.html"
    context_object_name = "book_titles"

    
    def get_queryset(self):
        return Book.objects.all().order_by('-created')
    