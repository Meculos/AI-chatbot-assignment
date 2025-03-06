from django.shortcuts import render
from rest_framework import generics, status, viewsets
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import (IsAuthenticated, AllowAny)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser, Chat
from .serializers import ChatSerializer, CustomUserSerializer

# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username", "").strip()
        password1 = request.data.get("password1", "")
        password2 = request.data.get("password2", "")

        if not username or not password1 or not password2:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        if password1 != password2:
            return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_password(password1)
        except ValidationError as e:
            return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        CustomUser.objects.create_user(username=username, password=password1)

        return Response({"message": "User successfully created"}, status=status.HTTP_201_CREATED)
    
class ChatView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Chat.objects.all()
        return Chat.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        if user.tokens < 100:
            raise ValidationError({"error": "Insufficient token balance"})
        
        user.tokens -= 100
        user.save()

        serializer.save(response="This AI model is currently offline. Please check back later.", user=user)

class UserGenericView(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

