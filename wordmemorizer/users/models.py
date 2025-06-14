from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Gerekirse ekstra alanlar ekleyebilirsin
    pass

class Word(models.Model):
    kelime = models.CharField(max_length=100)
    anlam = models.CharField(max_length=255)
    # kullanıcıya bağlamak istersen: user = models.ForeignKey(User, on_delete=models.CASCADE)