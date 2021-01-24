"""Animal serializers."""
#django Rest FrameWork
from rest_framework import serializers

#Model
from c_zoo.animals.models import Animal

class AnimalModelSerializer(serializers.ModelSerializer):
    """Animal model serializer."""
    
    class Meta:
        """Meta class."""
        
        model = Animal
        fields=(
            'name',
            'species',
            'color',
            'sex',
            'weight'
        )
    

# class AddAnimalSerializer(serializers.Serializer):
#     """Add animal"""
#     def create(self, data):
#         """Create a new animal"""
#         animal = Animal.objects.create()
#         return animal

