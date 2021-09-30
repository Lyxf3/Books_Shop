from django.contrib.auth.models import User, Group
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'price', 'issued', 'category', 'authors', 'publisher', available]

        def create(self, validated_data):
            return Book.objects.create(validated_data)

        def update(self, instance, validated_data):
            instance.title = validated_data


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'second_name']


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ['title']


class PromoCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PromoCode
        fields = ['percent', 'user', 'times_to_use', 'times_used']
