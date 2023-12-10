from .views import *
from django.urls import path


app_name = "book"
urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="categories"),
    path(
        "categories/<str:category_book_slug>",
        CategoryBooksDetailView.as_view(),
        name="category_books",
    ),
    path("", BookListView.as_view(), {"letter": None}, name="books"),
    path("<str:letter>/", BookListView.as_view(), name="book_detail"),
    path(
        "searched/books/result/<str:book_title>/",
        SearchedBooksListView.as_view(),
        name="searched_books_result",
    ),
]
