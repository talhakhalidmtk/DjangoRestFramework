from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from .models import Book, Review, Publisher, Contributor, BookContributor
from .serializers import BookSerializer, PublisherSerializer, ContributorSerializer, BookContributorSerializer, \
    ReviewSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny


class GenericModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            # Allow anonymous access to the list action
            permission_classes = [AllowAny]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]


class ContributorViewSet(GenericModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class BookContributorViewSet(GenericModelViewSet):
    queryset = BookContributor.objects.all()
    serializer_class = BookContributorSerializer


class PublisherViewSet(GenericModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class ReviewViewSet(GenericModelViewSet):
    queryset = Review.objects.order_by('-date_created')
    serializer_class = ReviewSerializer


class BookViewSet(GenericModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
