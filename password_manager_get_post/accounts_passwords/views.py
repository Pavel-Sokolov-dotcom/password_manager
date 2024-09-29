from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Password
from .serializers import PasswordSerializer
from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("FERNET_KEY")
if not key:
    raise ValueError('No Fernet key found in environment variables')

ciper = Fernet(key)

class PasswordViewSet(viewsets.ViewSet):
    def create(self, request, service_name):
        password = request.data.get('password')
        encrypted_password = ciper.encrypt(password.encode()).decode()
        password_obj, created = Password.objects.update_or_create(
            service_name=service_name,
            defaults={'encrypted_password': encrypted_password}
        )
        return Response({'service_name': password_obj.service_name, 'password': password}, status=status.HTTP_200_OK)

    def retrieve(self, request, service_name):
        try:
            password_obj = Password.objects.get(service_name=service_name)
            decrypted_password = ciper.decrypt(password_obj.encrypted_password.encode()).decode()
            return Response({'service_name': password_obj.service_name, 'password': decrypted_password})
        except Password.DoesNotExist:
            return Response({'error': 'Password not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        part_of_service_name = request.query_params.get('service_name', '')
        passwords = Password.objects.filter(service_name__icontains=part_of_service_name)
        serializer = PasswordSerializer(passwords, many=True)
        return Response(serializer.data)
