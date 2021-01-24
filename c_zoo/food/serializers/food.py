"""Food serializers."""
#django Rest FrameWork
from rest_framework import serializers

#Model
from c_zoo.food.models import Food

class FoodModelSerializer(serializers.ModelSerializer):
    """Food model serializer."""
    
    class Meta:
        """Meta class."""
        
        model = Food
        fields=(
            'food',
            'type_food',
            'stock'
        )
    