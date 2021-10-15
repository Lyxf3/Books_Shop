from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
# from rest_framework.decorators import action, list_route
# from rest_framework.response import Response
from user.serializers import UserSerializer
from user.models import User


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # @list_route()
    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # @action(methods=['get'])
    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)
    #
    # @action(methods=['post'])
    # def create(self, request):
    #     user = CustomUser.objects.create_user(
    #         name=request['name'],
    #         email=request['email'],
    #         is_staff=request['is_staff'],
    #         is_superuser=request['is_superuser'],
    #         is_active=request['is_active'],
    #         favourite_books=request['favourite_books'],
    #         balance=request['balance'],
    #     )
    #     user.save()
    #
    # @action(methods=['put'])
    # def update(self, request, pk=None):
    #     user = self.get_object(pk)
    #     serializer = UserSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
    #
    # @action(methods=['delete'])
    # def destroy(self, request, pk=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()

