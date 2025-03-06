from rest_framework import serializers
from .models import Chat, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "tokens"]
        read_only_fields = ["id", "username", "tokens"]

class ChatSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Chat
        fields = ["id", "username", "message", "response", "timestamp"]
        read_only_fields = ["id", "username", "response", "timestamp"]
