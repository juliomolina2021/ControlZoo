"""Delivey Food models"""
#Django
from django.db import models

#utilities
from c_zoo.utils.models import CZooModel

class Delivey_Food(CZooModel):
    """Food model"""

    fed_animal = models.ForeignKey('animals.Animal', on_delete=models.CASCADE, null= True)
    #distributor=models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    delivery_food=models.ForeignKey('food.Food', on_delete=models.CASCADE, null=True)
    quantity=models.CharField('amount of food', max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True)

    
    def __str__(self):
        """Return name."""
        return self.quantity