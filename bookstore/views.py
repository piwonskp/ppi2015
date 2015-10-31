from django.shortcuts import render
from django.views.generic.list import ListView

from bookstore.models import Book


class BookListView(ListView):
    model = Book
