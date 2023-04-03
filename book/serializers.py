from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Book, Publisher, Contributor, BookContributor


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'


class BookContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookContributor
        fields = ['contributor', 'role']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class BookSerializer(serializers.ModelSerializer):
    book_contributor = BookContributorSerializer(many=True)
    rating = serializers.SerializerMethodField('book_rating')
    reviews = serializers.SerializerMethodField('book_reviews')

    def create(self, validated_data):
        title = validated_data['title']
        publication_date = validated_data['publication_date']
        isbn = validated_data['isbn']
        cover = validated_data['cover']
        sample = validated_data['sample']
        publisher = validated_data['publisher']
        contributor = validated_data['book_contributor']['contributor']
        role = validated_data['book_contributor']['role']

        book = Book.objects.create(title=title, publication_date=publication_date, isbn=isbn, cover=cover,
                                   sample=sample, publisher=publisher)
        book.save()
        book.contributors.add(BookContributor(book=book, contributor=contributor, role=role))
        book.save()

        return book

    class Meta:
        model = Book
        fields = ('title', 'publication_date', 'isbn', 'cover', 'sample', 'publisher', 'book_contributor', 'rating',
                  'reviews',)
