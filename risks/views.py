from rest_framework import permissions, viewsets
from rest_framework.response import Response
from risks.models import Risk
from risks.permissions import IsUserRisk
from risks.serializers import RiskSerializer
from authentication.models import Account

class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.order_by('-created_at')
    serializer_class = RiskSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method is permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),IsUserRisk(),)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)

        return super(RiskViewSet, self).perform_create(serializer)

class UserRisksViewSet(viewsets.ViewSet):
    queryset = Risk.objects.select_related('user').all()
    serializer_class = RiskSerializer

    def list(self, request):
        account = Account.objects.get(username=account_username)
        account_uid = account.get_uid()
        queryset = self.queryset.filter(id=account_uid)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
