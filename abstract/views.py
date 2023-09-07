
#! Django function and methods
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


#!Models,Forms and Serializer classes
from apps.book.models import Book,BookTitle



#?changeTheme
@login_required
def changeTheme(request):
    if 'is_dark_mode' in request.session:                                                                                       
        request.session['is_dark_mode'] = not request.session['is_dark_mode']
    else:
        request.session['is_dark_mode'] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


#!?getHomeView
def getHomeView(request):
    #set dark mode
    # if 'is_dark_mode' in request.session:                                                                                       
    #     request.session['is_dark_mode'] = not request.session['is_dark_mode']
    # else:
    #     request.session['is_dark_mode'] = True
    
    #get all books
    titlebooks = BookTitle.objects.get(id=25)
    books = titlebooks.books
    context = {
        'books': books
    }
    return render(request,'abstract/main.html',context)




