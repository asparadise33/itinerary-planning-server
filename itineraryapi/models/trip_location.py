from django.db import models
from .location import Location

class TripLocation(models.Model):
   # trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='locationTrips')
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='tripLocations')
