from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'contributors', views.ContributorViewSet)

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('', include((router.urls, 'api'))),
]
