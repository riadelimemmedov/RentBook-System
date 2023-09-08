from .views import *
from django.urls import path


app_name='book'
urlpatterns = [
    path('',BookListView.as_view(),name='books'),
]
