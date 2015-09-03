from rest_framework import serializers
from authentication.serializers import Account, AccountSerializer
from risks.models import Risk

class RiskSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True, required=False)

    class Meta:
        model = Risk
        fields = ('id', 'user', 'code', 'duration', 'created_at', 'updated_at')

        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(RiskSerializer, self).get_validations_exclusions()

        return exclusions + ['user']