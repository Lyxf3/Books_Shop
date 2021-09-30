from django.shortcuts import render

# Create your views here.
from book.models import Book
from rest_framework import viewsets
from rest_framework import permissions
from book.serializers import BookSerializer, AuthorSerializer, \
    PublisherSerializer, PromoCodeSerializer


class BookGetAll(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookGet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    
class BookPost(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdate(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BooDelete(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


