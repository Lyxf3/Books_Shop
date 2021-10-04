from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from user.serializers import UserSerializers
from user.models import User


class UserViewSet(viewsets.ViewSet):

    @list_route()
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @detail_route(methods=['post'])
    def create(self, request):
        user = CustomUser.objects.create_user(
            name=request['name'],
            email=request['email'],
            is_staff=request['is_staff'],
            is_superuser=request['is_superuser'],
            is_active=request['is_active'],
            favourite_books=request['favourite_books'],
            balance=request['balance'],
        )
        user.save()

    @detail_route(methods=['put'])
    def update(self, request, pk=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @detail_route(methods=['delete'])
    def destroy(self, request, pk=None):
        snippet = self.get_object(pk)
        snippet.delete()

