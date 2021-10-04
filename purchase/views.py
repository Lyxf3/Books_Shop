from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from book.serializers import (
    CategorySerializers, AuthorSerializers, BookSerializers, PromoCodeSerializers
)
from purchase.models import (
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

