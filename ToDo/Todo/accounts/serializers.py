from django.db import models
from django.db.models import fields
from rest_framework import serializers
from accounts.models import Accounts


class RegistrationSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(style={'input_type': 'password', write_only = True})
    class Meta:
        model = Accounts
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Accounts(**validated_data)
        user.set_password(password)
        user.save()
        return user
