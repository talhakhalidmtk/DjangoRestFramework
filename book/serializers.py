from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated, PermissionDenied

from .models import Book, Publisher, Review, Contributor, BookContributor
from .utils import average_rating


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'


class BookContributorSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    contributor = serializers.PrimaryKeyRelatedField(queryset=Contributor.objects.all())

    class Meta:
        model = BookContributor
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()
    rating = serializers.SerializerMethodField('book_rating')
    reviews = serializers.SerializerMethodField('book_reviews')

    def book_rating(self, book):
        reviews = book.review_set.all()
        if reviews:
            return average_rating([review.rating for review in reviews])
        else:
            None

    def book_reviews(self, book):
        reviews = book.review_set.all()
        if reviews:
            return ReviewSerializer(reviews, many=True).data
        else:
            None

    def to_representation(self, instance):
        # Call the parent class's to_representation() method
        representation = super().to_representation(instance)

        contributors = instance.bookcontributor_set.all()
        representation['contributors'] = [
            {
                'first_name': contributor.contributor.first_names,
                'last_name': contributor.contributor.last_names,
                'role': contributor.role
            } for contributor in contributors
        ]

        return representation

    class Meta:
        model = Book
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = '__all__'

    def perform_update(self, serializer):
        request = self.context['request']
        creator = request.user
        if serializer.instance.creator_id != creator.pk:
            raise PermissionDenied('Permission denied, you are not the creator of this review')
        serializer.save(date_edited=timezone.now())
