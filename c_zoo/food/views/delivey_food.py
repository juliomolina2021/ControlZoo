"""Delivey_food views."""

# Django REST Framework
from rest_framework.views import APIView
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
#
from django.db.models import Avg, Sum
# Models
from c_zoo.food.models  import Delivey_Food

# Serializers
from c_zoo.food.serializers import DeliveryFoodModelSerializer
from c_zoo.users.serializers import UserModelSerializer

class DeliveryFoodViewSet(
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet
                    ):
    """Food view set."""
    
    queryset= Delivey_Food.objects.all()
    serializer_class= DeliveryFoodModelSerializer
    
    # def post(self, request):
    #     serializer = DeliveryFoodModelSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     delivery=serializer.save()
    #     data=DeliveryFoodModelSerializer(delivery).data
        
    #     return Response(data, status=status.HTTP_201_CREATE)

class resultados(APIView):   
    def total_fed_food(self, request, animal):
        queryset=Delivey_Food.objects.get(fed_animal=animal).aggregate(sum('delivery_food'))
        serializer=DeliveryFoodModelSerializer(queryset)
        return  Response(serializer.data, status=status.HTTP_200_OK)
