from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from book.serializers import (
    CategorySerializer, AuthorSerializer, BookSerializer, PromoCodeSerializer
)
from book.models import (
    Category, Author, Book, PromoCode
)

from django.db.models import Avg, Max


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # @list_route()
    # def get_avg_author_discount(self, request):
    #     queryset = Book.objects.all()
    #     serializer = BookSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # @detail_route(methods=['get'])
    # def retrieve(self, request, pk=None):
    #     queryset = Book.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = BookSerializer(user)
    #     return Response(serializer.data)


class PromoCodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer

    # @list_route()
    # def list(self, request):
    #     queryset = PromoCode.objects.all()
    #     serializer = PromoCodeSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # @detail_route(methods=['get'])
    # def retrieve(self, request, pk=None):
    #     queryset = PromoCode.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = PromoCodeSerializer(user)
    #     return Response(serializer.data)


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    #
    # @list_route()
    # def list(self, request):
    #     queryset = PromoCode.objects.all()
    #     serializer = PromoCodeSerializer(queryset, many=True)
    #     return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # @list_route()
    # def list(self, request):
    #     queryset = Category.objects.all()
    #     serializer = CategorySerializer(queryset, many=True)
    #     return Response(serializer.data)

