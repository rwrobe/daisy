from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from authentication.models import Account
from authentication.serializers import AccountSerializer
from django.utils.translation import ugettext as _

# From REST framework
class AccountViewSet(viewsets.ModelViewSet):
    # Define the query
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    # Class method to check permissions on POST
    def get_permissions(self):
        # Alright, is this dude trying to update or delete existing data?
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        # Allow anyone to create an account
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        # Let's see if this user is logged in and if they are trying to mess with their own stuff
        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    # Override the create method so the password isn't saved literally
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(
                serializer.validated_data, status=status.HTTP_201_CREATED
            )

        # If it isn't valid...
        return Response({
            'status': 'Bad request',
            'message': _('Your account could not be created. Please contact an administrator, or just do it right next time.')
        }, status=status.HTTP_400_BAD_REQUEST)