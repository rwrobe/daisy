from rest_framework import viewsets, views, status, permissions
from rest_framework.response import Response
from authentication.models import Account
from authentication.serializers import AccountSerializer
from django.utils.translation import ugettext as _
import json
from django.contrib.auth import authenticate, login, logout
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

# Login API View
class LoginView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password')

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': _('Sorry, we disabled this account. Please contact an admin.')
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': _('Incorrect user/password combination')
            }, status=status.HTTP_401_UNAUTHORIZED)

# Logout View
class LogoutView(views.APIView):
    permissions = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)