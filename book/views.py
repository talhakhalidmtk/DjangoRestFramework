from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from .models import Book, Review, Publisher, Contributor, BookContributor
from .serializers import BookSerializer, PublisherSerializer, ContributorSerializer, BookContributorSerializer, \
    ReviewSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            # Allow anonymous access to the list action
            permission_classes = [AllowAny]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]


class BookContributorViewSet(viewsets.ModelViewSet):
    queryset = BookContributor.objects.all()
    serializer_class = BookContributorSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            # Allow anonymous access to the list action
            permission_classes = [AllowAny]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            # Allow anonymous access to the list action
            permission_classes = [AllowAny]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.order_by('-date_created')
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            # Allow anonymous access to the list action
            permission_classes = [AllowAny]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            # Allow anonymous access to the list action
            permission_classes = [AllowAny]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]
