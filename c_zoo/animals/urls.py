"""Animals URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import animals as animal_views


router = DefaultRouter()
router.register(r'animals', animal_views.AnimalViewSet, basename='animals')

urlpatterns = [
    path('', include(router.urls)),
]