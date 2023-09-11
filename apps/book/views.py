
#! Django function and methods
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import ListView,FormView


#!Models,Forms and Serializer classes
from .models import Book,BookTitle
from .forms import BookTitleForm


# Create your views here.



#?BookTitleListView
class BookListView(FormView):
    model = Book
    form_class = BookTitleForm
    template_name = "book/book.html"
    context_object_name = "book_titles"
    # success_url = reverse_lazy('book:books') If you want redirect to other page after some process
    
    
    def get_success_url(self):#If you want modify url before redirect to other page
        return self.request.path
    

    
    def get_queryset(self):
        return Book.objects.all().order_by('-created')
    
    
    
    @classmethod
    def is_ajax(cls, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    
    def form_valid(self, form):
        instance = form.save(commit=False)
        if self.is_ajax(self.request) and form.is_valid:
            instance.save()
            return JsonResponse({'success': True})
        return super(BookListView, self).form_valid(form)

