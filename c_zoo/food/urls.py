"""Food URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import food as food_views
from .views import delivey_food as delivey_views


router = DefaultRouter()
router.register(r'food', food_views.FoodViewSet, basename='food')
router.register(r'delivery_food', delivey_views.DeliveryFoodViewSet, basename='delivey_food')
# router.register(r'delivery_food/total_fed_food/<str:pk>',delivey_views.DeliveryFoodViewSet, basename='delivey_food_total')

urlpatterns = [
    path('', include(router.urls)),
    #path('delivery_food/total_fed_food/<str:pk>',delivey_views.DeliveryFoodViewSet, name='delivey_food_total')
    # path('food', food_views.FoodViewSet, name='food'),
    # path('delivery_food', delivey_views.DeliveryFoodViewSet, name='delivey_food'),
    # path('delivery_food/total_fed_food/<str:animal>', delivey_views.resultados, name='total_fed_food'),
]