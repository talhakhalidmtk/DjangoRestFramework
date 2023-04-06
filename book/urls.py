from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='books')
router.register(r'reviews', views.ReviewViewSet, basename='reviews')
router.register(r'publishers', views.PublisherViewSet, basename='publishers')
router.register(r'contributors', views.ContributorViewSet, basename='contributors')
router.register(r'book_contributors', views.BookContributorViewSet, basename='book_contributors')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('accounts/', include('rest_registration.api.urls')),
    path('', include((router.urls, 'api'))),
]
