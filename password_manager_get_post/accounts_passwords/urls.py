from django.urls import path
from .views import PasswordViewSet

urlpatterns = [
    path('password/<str:service_name>/', PasswordViewSet.as_view({'post': 'create', 'get': 'retrieve'}), name='password-retrieve'),
    path('password/', PasswordViewSet.as_view({'get': 'list', 'post': 'create'}), name='password-create'),
]   
