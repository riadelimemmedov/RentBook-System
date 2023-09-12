
#! Django function and methods
from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView,FormView
from django.utils.html import strip_tags


#!Models,Forms and Serializer classes
from .models import Book,BookTitle
from .forms import BookTitleForm


# Create your views here.



#?BookTitleListView
class BookListView(ListView,FormView):
    model = Book
    form_class = BookTitleForm
    template_name = "book/book.html"
    context_object_name = "book_titles"
    # success_url = reverse_lazy('book:books') If you want redirect to other page after some process
    
    
    def get_success_url(self):#If you want modify url before redirect to other page
        return self.request.path
    

    
    def get_queryset(self):
        return Book.objects.all().order_by('-created')
    
    
    def get_context_data(self,**kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['name'] = 'John'
        context['form'] = self.get_form_class()
        context['qs'] = self.get_queryset()
        
        return context
    
    @classmethod
    def is_ajax(cls, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    
    def form_valid(self, form):
        instance = form.save(commit=False)
        if self.is_ajax(self.request) and form.is_valid():
            instance.save()
            return JsonResponse({'success': True},status=200)
        else:
            pass
        return super(BookListView, self).form_valid(form)
    
    
    def form_invalid(self,form):
        form_errors = self.handleFormErrors(form)
        if form_errors:        
            return JsonResponse({'form_errors': form_errors},status=400)
        return super(BookListView, self).form_valid(form)

    
    def handleFormErrors(self,form):
        error_messages = []
        for field_name, errors in form.errors.items():
            for error in errors:
                error_messages.append(strip_tags({field_name:error}))
        return error_messages