from django.db import models
from .location import Location
from .trip import Trip

class TripLocation(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='locationTrips')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='tripLocations')
