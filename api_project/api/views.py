from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.


class BookList(generics.ListAPIView):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
