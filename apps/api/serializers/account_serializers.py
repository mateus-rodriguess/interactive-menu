from django.db.models.base import Model
from apps.account.models import User
from rest_framework import serializers
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response


class AccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["pk", "username", "CPF", 'email', 'is_staff', 'is_active']


class AccountCreateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["username", "CPF", 'email']
    
    def create(self, validated_data):

        return super().create(validated_data)


class AccountDeleteSerializers(serializers.ModelSerializer, DestroyModelMixin):
    
    class Meta:
        model = User
        fields = ["CPF", 'email', 'is_staff', 'is_active']

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class AccountUpdateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["password", "CPF", 'email']

    def update(self, instance, validated_data):
        
        return super().update(instance, validated_data)