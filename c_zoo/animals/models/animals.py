"""Animals models"""
#Django
from django.db import models

#utilities
from c_zoo.utils.models import CZooModel

class Animal(CZooModel):
    """Animal model"""
    
    name= models.CharField('animal name', max_length=100)
    species=models.CharField('animal species', max_length=100)
    color=models.CharField('animal name', max_length=50)
    sex=models.CharField('animal name', max_length=25)
    weight=models.FloatField(blank= True, null=True)
    
    def __str__(self):
        """Return name."""
        return self.name