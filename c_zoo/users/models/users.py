#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#utilities
from c_zoo.utils.models import CZooModel

class User(CZooModel, AbstractUser):
    """User model.
    Extend from Django's user, change the username field
    to email and add some extra fields.
    """
    email= models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique':'A user with that email already exists.'
        }
    )

    phone_regex=RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +99999999. up to 15 digits allowed."
    )

    phone_number=models.CharField(validators=[phone_regex],max_length=17, blank=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']
    
    is_client=models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries.'
            'Clients are the main type of user.'
        )
    )
    
    is_verified=models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address.'
    )
    
    is_admin = models.BooleanField(
        'administrator',
        default=False,
        blank=True,
        null=True,
        help_text="Administrator admins can create news animals."
    )
    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username








