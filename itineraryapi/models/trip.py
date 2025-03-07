from django.db import models
from django.utils import timezone
from itineraryapi.models import User, TravelMode
class Trip(models.Model):
    """Trip Model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userTrips")
    destination = models.CharField(max_length=255)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    mode_of_travel = models.ForeignKey(TravelMode, on_delete=models.CASCADE, related_name="travelMode")
    number_of_travelers = models.IntegerField()
    people_on_trip = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-start_date',)
