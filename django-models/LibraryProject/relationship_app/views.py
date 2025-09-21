from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Author, Book, Library, Librarian

# Create your views here.


def book_list(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/book_list.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
