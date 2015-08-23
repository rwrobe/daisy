from rest_framework import serializers
from authentication.serializers import Account, AccountSerializer
from risks.models import Risk, Transportation, Sedentary, Activity

class RiskSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True, required=False)

    class Meta:
        model = Risk

        fields = ('id', 'user', )