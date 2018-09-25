from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from appAccounts.models import User
from appAccounts.serializers import *
from appAccounts.permissions import *


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UsersSerializer

    # def get_object(self):
    #     print('get-object ->\t', self.kwargs)
    #     obj = get_object_or_404(self.get_queryset(), email='')
    #     self.check_object_permissions(self.request, obj)
    #     return obj
    #
    # def retrieve(self, request, email=None, **kwargs):
    #     print('retrieve ->\t', email, kwargs)

    def post(self, request, format='json'):
        serializer = UsersSerializer(data=request.data)
        print('post ->\t', serializer)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),

    @action(methods=['get'], detail=False, url_path='(?P<email>\S+)')
    def exist(self, request, email, ):
        user = get_object_or_404(User, email=email)
        return Response(UsersSerializer(user).data, status=status.HTTP_200_OK)
