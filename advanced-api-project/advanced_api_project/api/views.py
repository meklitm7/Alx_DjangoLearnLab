from django.shortcuts import render
from rest_framework import generics, permissions,filters
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# List + Create Books

class BookListCreateAPIView(generics.ListCreateAPIView):

  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  filterset_fields = ["title", "author__name", "publication_year"]
  search_fields = ["title", "author__name"]
  ordering_fields = ["title", "publication_year"]
  
# Retrieve + Update + Delete Book
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
