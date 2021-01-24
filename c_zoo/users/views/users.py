"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
#from rest_framework.views import APIView

from c_zoo.users.serializers import (
    AccountVerificationSerializer,
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
    )

#models
from c_zoo.users.models import User

class UserViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
    ):
    """
    User View set 
    handle sing up, login and account verification.
    """
    queryset= User.objects.filter(is_active=True, is_client=True)
    serializer_class= UserModelSerializer
    lookup_field='username'
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        """ User login"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data={
            'user':UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status= status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def signup(self, request):
        """ User Sign up"""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data={
            'user':UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status= status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['Post'])
    def verify(self, request):
        """Account verificaction"""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data={'message':'Congratulations your account verification, is succesful'}      
        
        return Response(data, status= status.HTTP_200_OK)