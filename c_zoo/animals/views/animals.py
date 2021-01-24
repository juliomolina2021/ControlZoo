"""Animals views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Models
from c_zoo.animals.models import Animal

# Permissions
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from c_zoo.animals.permissions.animals import IsUserAdmin
# Filters
# from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from c_zoo.animals.serializers import AnimalModelSerializer

class AnimalViewSet(
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet
                    ):
    """Animal view set."""
    
    queryset= Animal.objects.all()
    serializer_class= AnimalModelSerializer
    lookup_field='name'
    
    # def post(self, request,*args, **kwargs):
    #     serializer = AnimalModelSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     animal=serializer.save()
    #     data=AnimalModelSerializer(animal).data
        
    #     return Response(data, status=status.HTTP_201_CREATED)


    
    def get_permissions(self):
        """Assign permisssions based on action."""
        
        if self.action == 'list':
            permissions=[AllowAny]
        elif self.action=='create':
            permissions=[IsUserAdmin, IsAuthenticated]
        else:
            permissions=[IsAuthenticated]
        return [permission() for permission in permissions]

