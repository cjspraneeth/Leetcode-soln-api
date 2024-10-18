# scraper/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProblemViewSet

router = DefaultRouter()
router.register(r'problems', ProblemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
