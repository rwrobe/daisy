from rest_framework import serializers
from authentication.models import Account
from django.contrib.auth import update_session_auth_hash

class AccountSerializer(serializers.ModelSerializer): # DRF naming convention
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account # Model to serialize
        fields = ('id','email','username','first_name','last_name','location', 'created_at','updated_at', 'password','confirm_password') # Fields to serialize
        read_only_fields = ('created_at','updated_at')

    def create(self, validated_data):
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Data validation, yo
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.location = validated_data.get('location',instance.location)
        instance.created_at = validated_data.get('created_at',instance.created_at)
        instance.updated_at = validated_data.get('updated_at',instance.updated_at)

        instance.save()

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

        return instance