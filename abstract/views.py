
#! Django function and methods
from django.shortcuts import render

# Create your views here.


#!Models,Forms and Serializer classes
from apps.book.models import Book,BookTitle


def getHomeView(request):
    titlebooks = BookTitle.objects.get(id=2)
    books = titlebooks.books
    context = {
        'books': books
    }
    return render(request,'abstract/main.html',context)