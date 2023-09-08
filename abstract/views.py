
#! Django function and methods
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView

# Create your views here.


#!Models,Forms and Serializer classes
from apps.book.models import Book,BookTitle



#?changeTheme
@csrf_exempt
def changeTheme(request):
    if 'is_dark_mode' in request.session:                                                                                       
        request.session['is_dark_mode'] = not request.session['is_dark_mode']
    else:
        request.session['is_dark_mode'] = True
    return JsonResponse({'is_dark_mode':request.session['is_dark_mode']})



#?BookTitleListView
class BookTitleListView(ListView):
    model = BookTitle
    template_name = "abstract/main.html"
    context_object_name = "book_titles"
    
    
    def get(self,request,*args,**kwargs):
        request.session['page_reload_count'] = 0    
        page_reload_count = request.session['page_reload_count']
        
        if request.method == 'GET':
            page_reload_count += 1
            request.session['page_reload_count'] = page_reload_count

        print('Get request coming ', page_reload_count)
        return super(BookTitleListView,self).get(request, *args, **kwargs)
    




