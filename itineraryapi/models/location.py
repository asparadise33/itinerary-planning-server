from django.db import models

class Location(models.Model):
    place_name = models.CharField(max_length=100)
  