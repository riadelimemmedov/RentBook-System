#! Django function and methods
from typing import Any
from django import http
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, FormView
from django.utils.html import strip_tags
from django.core import serializers
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


#!Models,Forms and Serializer classes
from .models import Book, BookTitle
from .forms import BookTitleForm


#!Python modules and functions
import string

# Create your views here.


# ?BookTitleListView
class BookListView(ListView, FormView):
    model = Book
    form_class = BookTitleForm
    template_name = "book/book.html"
    context_object_name = "book_titles"
    # success_url = reverse_lazy('book:books') If you want redirect to other page after some process

    def get_success_url(self):  # If you want modify url before redirect to other page
        return self.request.path

    def get(self, request, *args, **kwargs):
        if self.is_ajax(request):
            parameter = kwargs.get("letter", "A")
            books_titles = BookTitle.objects.filter(book_title__startswith=parameter)
            data = serializers.serialize("json", books_titles)
            return JsonResponse({"book_titles": data}, safe=False, status=200)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        letters = list(string.ascii_uppercase)
        context["letters"] = letters
        return context

    @classmethod
    def is_ajax(cls, request):
        return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"

    def form_valid(self, form):
        instance = form.save(commit=False)
        if self.is_ajax(self.request) and form.is_valid():
            instance.save()
            return JsonResponse({"success": True}, status=200)
        else:
            pass
        return super(BookListView, self).form_valid(form)

    def form_invalid(self, form):
        form_errors = self.handleFormErrors(form)
        if form_errors:
            return JsonResponse({"form_errors": form_errors}, status=400)
        return super(BookListView, self).form_valid(form)

    def handleFormErrors(self, form):
        error_messages = []
        for field_name, errors in form.errors.items():
            for error in errors:
                error_messages.append(strip_tags({field_name: error}))
        return error_messages


# ?SearchedBooksListView
class SearchedBooksListView(ListView):
    model = Book
    template_name = "book/searched_books.html"
    context_object_name = "books"
    paginate_by = 2
    books = None

    @classmethod
    def is_ajax(cls, request):
        return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"

    def get_queryset(self, **kwargs):
        searched_keyword = self.request.path.split("/")[-2]
        self.books = Book.objects.filter(title__book_title__icontains=searched_keyword)
        return self.books

    # If you want add ajax search functionality
    # def render_to_response(self,context,**response_kwargs):
    #     if self.is_ajax(self.request):
    #         paginator = Paginator(self.books, 2)
    #         page = self.request.GET.get('page')
    #         paged_books = paginator.get_page(page)
    #         has_previous = paged_books.has_previous()
    #         has_next = paged_books.has_next()
    #         previous_page_number = paged_books.previous_page_number()
    #         next_page_number = paged_books.next_page_number()
    #         if paged_books:
    #             data = []
    #             for obj in paged_books:
    #                 item = {
    #                     "id":obj.id,
    #                     "title":obj.title.book_title,
    #                     "book_isbn":obj.book_isbn
    #                 }
    #                 data.append(item)
    #             return JsonResponse({'paged_books':data,"has_previous":has_previous,"has_next":has_next,"previous_page_number":previous_page_number,"next_page_number":next_page_number},safe=False)
    #     return super().render_to_response(context,**response_kwargs)
