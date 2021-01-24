"""Food models"""
#Django
from django.db import models

#utilities
from c_zoo.utils.models import CZooModel

class Food(CZooModel):
    """Food model"""
    food=models.CharField('name food', max_length=100)
    type_food= models.CharField('type food', max_length=100)
    stock=models.FloatField(blank= True, null=True)
    
    def __str__(self):
        """Return name."""
        return self.food