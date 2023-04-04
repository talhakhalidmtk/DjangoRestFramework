from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'contributors', views.ContributorViewSet)
router.register(r'book_contributors', views.BookContributorViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('accounts/', include('rest_registration.api.urls')),
    path('', include((router.urls, 'api'))),
]
