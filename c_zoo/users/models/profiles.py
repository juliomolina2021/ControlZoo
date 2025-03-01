"""profile model."""

from django.db import models

#utilities
from c_zoo.utils.models import CZooModel

class Profile(CZooModel):
    """
    Profile model.
    a profile holds a user's public data like biography, picture,
    and statistics
    """
    user= models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture= models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography= models.TextField(max_length=500, blank=True)

    #stats
    # rides_taken=models.PositiveIntegerField(default=0)
    # rides_offered=models.PositiveIntegerField(default=0)
    # reputation = models.FloatField(
    #     default=5.0,
    #     help_text="user's reputation based on the rides taken and offered"
    # )

    def __str__(self):
        """Return user's str representation"""
        return str(self.user)


