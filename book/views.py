from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from book.serializers import (
    CategorySerializers, AuthorSerializers, BookSerializers, PromoCodeSerializers
)
from book.models import (
    Category, Author, Book, PromoCode
)


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    @list_route()
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(user)
        return Response(serializer.data)


class PromoCodeViewSet(viewsets.ReadOnlyModelViewSet):
    @list_route()
    def list(self, request):
        queryset = PromoCode.objects.all()
        serializer = PromoCodeSerializer(queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def retrieve(self, request, pk=None):
        queryset = PromoCode.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PromoCodeSerializer(user)
        return Response(serializer.data)


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    @list_route()
    def list(self, request):
        queryset = PromoCode.objects.all()
        serializer = PromoCodeSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    @list_route()
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

