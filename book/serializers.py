from django.contrib.auth.models import (
    Book, Author, Publisher, PromoCode
)
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def get_all(self):
        return Book.objects.all()

    def get(self, pk):
        return Book.objects.get(pk=pk)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    def get_all(self):
        return Author.objects.all()

    def get(self, pk):
        return Author.objects.get(pk=pk)


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"

    def get_all(self):
        return Publisher.objects.all()

    def get(self, pk):
        return Publisher.objects.get(pk=pk)


class PromoCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PromoCode
        fields = "__all__"

    def get_all(self):
        return PromoCode.objects.all()

    def get(self, pk):
        return PromoCode.objects.get(pk=pk)


