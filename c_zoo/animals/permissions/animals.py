"""User permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from c_zoo.users.models import User

class IsUserAdmin(BasePermission):
    """Allow access only admins to register animals."""

    def has_object_permission(self, request, view, obj):

        try:
            User.objects.get(
                user=request.user,
                is_admin=True
            )
        except User.DoesNotExist:
            return False
        return True
