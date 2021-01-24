"""Django models utilities."""
#djangl
from django.db import models

class CZooModel(models.Model):
    """Comparte Ride base model.

    CZoo act as an abastract base class from whiche every
    other model in the project will inherit. htis class provides
    every table with the following attributes:
        create:(Datetime): store the date time the object whas created.
        modified:(Datetime): store the last date tieme the object was modified.
    """

    created=models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified=models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """ Meta option."""
        abstract= True

    get_latest_by = 'created'
    ordering=['-created','-modified']
