from rest_framework import serializers
from .models import Client, ConflictCheck


class ClientSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    lawyer_name = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'lawyer')

    def get_lawyer_name(self, obj):
        return obj.lawyer.get_full_name() or obj.lawyer.username

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone must contain digits only.")
        if len(value) < 10:
            raise serializers.ValidationError("Phone must be at least 10 digits.")
        return value


class ConflictCheckSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()
    checked_by_name = serializers.SerializerMethodField()

    class Meta:
        model = ConflictCheck
        fields = '__all__'
        read_only_fields = ('checked_at', 'checked_by')

    def get_client_name(self, obj):
        return obj.client.full_name

    def get_checked_by_name(self, obj):
        return obj.checked_by.username