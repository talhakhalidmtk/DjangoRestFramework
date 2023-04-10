from rest_framework import viewsets
from django.utils import timezone
from .permissions import VerifyCreator
from .serializers import BookSerializer, PublisherSerializer, ContributorSerializer, BookContributorSerializer, \
    ReviewSerializer

from rest_framework.permissions import AllowAny


class GenericModelViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        model = self.serializer_class.Meta.model
        queryset = model.objects.all()
        return queryset

    def get_permissions(self):
        if self.action == 'list':
            # Allow anonymous access to the list action
            permission_classes = [AllowAny]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]


class ContributorViewSet(GenericModelViewSet):
    serializer_class = ContributorSerializer


class BookContributorViewSet(GenericModelViewSet):
    serializer_class = BookContributorSerializer


class PublisherViewSet(GenericModelViewSet):
    serializer_class = PublisherSerializer


class BookViewSet(GenericModelViewSet):
    serializer_class = BookSerializer


class ReviewViewSet(GenericModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [VerifyCreator]

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-date_created')
        return queryset

    def get_permissions(self):
        permission_classes = super().get_permissions()
        permission_classes += [permission() for permission in self.permission_classes]
        return permission_classes

    def perform_update(self, serializer):
        serializer.save(date_edited=timezone.now())
