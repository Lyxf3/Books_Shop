from book.models import (
    Book, Author, Publisher, PromoCode, Category
)
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'price', 'issued', 'categories', 'authors', 'publisher',
                  'market_id', 'discount_shop', 'discount_market', 'available')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'second_name', 'percent')


class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = ('id', 'percent', 'user', 'times_to_use', 'times_used')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)
