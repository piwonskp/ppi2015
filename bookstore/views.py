from django.views.generic.list import ListView

from bookstore.models import Book


class BookListView(ListView):
    model = Book

    def get_queryset(self):
        title = self.request.GET.get('title', '')
        queryset = Book.objects.filter(title__icontains=title)
        return queryset
