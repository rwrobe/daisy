from rest_framework import permissions, viewsets
from rest_framework.response import Response
from risks.models import Risk
from risks.permissions import IsUserRisk
from risks.serializers import RiskSerializer

class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.order_by('-created_at')
    serializer_class = RiskSerializer

    def get_permissions(self):
        if self.request.method is permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),IsUserRisk(),)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)

        return super(RiskViewSet, self).perform_create(serializer)

class UserRisksViewSet(viewsets.ViewSet):
    queryset = Risk.objects.select_related('user').order_by('-created_at')
    serializer = RiskSerializer

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(user = account_username)
        serialized = self.serializer_class(queryset, many=True)

        return Response(serialized.data)
