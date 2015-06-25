from rest_framework import permissions, viewsets

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    """
    Views for listing, creating, retrieving, updating and destroying Account instances.
    """
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        # Allow safe methods like GET but resrict everything else to account owner 
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        # Explicitly allow account creation by any/all
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            """
            Use Account.objects.create_user() instead of save() to
            properly hash & salt password.
            """
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)