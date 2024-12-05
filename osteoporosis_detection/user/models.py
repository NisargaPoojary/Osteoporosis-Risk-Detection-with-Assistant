from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username
