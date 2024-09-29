from django.db import models

class Password(models.Model):
    service_name = models.CharField(max_length=255, unique=True)
    encrypted_password = models.TextField()
    
    def __str__(self):
        return self.service_name