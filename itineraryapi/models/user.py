from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=50)
    uid = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
