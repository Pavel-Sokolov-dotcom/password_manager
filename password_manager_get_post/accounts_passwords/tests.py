from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Password
import json

class PasswordViewSetTests(APITestCase):
    
    def setUp(self):
        self.service_name = 'yundex'
        self.password_data = {
            'password': 'very_secret_pass'
        }
        self.url_create = reverse('password-retrieve', args=[self.service_name])  
        self.url_retrieve = reverse('password-retrieve', args=[self.service_name])
    
    def test_create_password(self):
        response = self.client.post(self.url_create, data=json.dumps(self.password_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_retrieve_password(self):

        self.client.post(self.url_create, data=json.dumps(self.password_data), content_type='application/json')
  
        response = self.client.get(self.url_retrieve)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['password'], self.password_data['password'])
