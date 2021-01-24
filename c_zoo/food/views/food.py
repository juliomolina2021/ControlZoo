"""Food views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Models
from c_zoo.food.models import Food

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from c_zoo.food.serializers import FoodModelSerializer

class FoodViewSet(
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet
                    ):
    """Food view set."""
    
    queryset= Food.objects.all()
    serializer_class= FoodModelSerializer
    
    # def post(self, request,*args, **kwargs):
    #     serializer = FoodModelSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     Food=serializer.save()
    #     data=FoodModelSerializer(Food).data
        
    #     return Response(data, status=status.HTTP_201_CREATED)