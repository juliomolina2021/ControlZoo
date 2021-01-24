"""Deliver_Food serializers."""
#django Rest FrameWork
from rest_framework import serializers

from c_zoo.animals.serializers import AnimalModelSerializer
from c_zoo.food.serializers import FoodModelSerializer

#Model
from c_zoo.food.models import Delivey_Food

class DeliveryFoodModelSerializer(serializers.ModelSerializer):
    """Delivery_Food model serializer."""
    #fed_animal= AnimalModelSerializer()
    #fed_animal= serializers.StringRelatedField()

    #delivey_food=delivey_fo()
    class Meta:
        """Meta class."""
        
        model = Delivey_Food
        fields=(
            'fed_animal',
            'quantity',
            'delivery_food',
            'date',
            'comments'
        )
    
    def to_representation(self, instance):
        return{
            'fed_animal':instance.fed_animal.name,
            'quantity':instance.quantity,
            'delivery_food':instance.delivery_food,
            'date':instance.date,
            'comments':instance.comments
        }
        
        
        
        