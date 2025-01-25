from django.db import models

class TravelMode(models.Model):
    type_of_travel = models.CharField(max_length=100)
