from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from itineraryapi.models import User, TravelMode, Trip, Location
from itineraryapi.views.trip import TripSerializer
# TODO: DOESN'T WORK 
#     KeyError: 'uid'
class TripTests(APITestCase):

  fixtures = ['user', 'trip', 'location', 'mode']
  def setUp(self):
    self.user = User.objects.first()
    
  def test_create_trip(self):
    """Create Trip Test"""
    """Create Trip Test"""
    url = "/trips"
    
    trip = {
      "user": 1,
      "destination": "Turkey",
      "start_date": "2025-01-27",
      "end_date": "2025-01-27",
      "mode_of_travel": 1,
      "number_of_travelers": 2,
      "people_on_trip": "Bill and Ted",
      "notes": "We trippin",
      "created_at": "2025-01-28T00:57:10.647643Z",
      "updated_at": "2025-01-28T00:57:10.648641Z"
      
    }
    response = self.client.post(url, trip, format='json')
    new_trip = Trip.objects.last()
    expected = TripSerializer(new_trip)
    self.assertEqual(expected.data, response.data)
    
 