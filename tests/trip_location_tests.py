from rest_framework import status
from rest_framework.test import APITestCase
from itineraryapi.models import Location, Trip, TripLocation
from itineraryapi.views.trip_location import TripLocationSerializer
class TripLocationTests(APITestCase):
    fixtures = ['location', 'trip', 'triplocation', 'user', 'mode']
    def setUp(self):
        self.triplocation = TripLocation.objects.first()
        self.location = Location.objects.first()
        self.trip = Trip.objects.first()
    def test_create_triplocation(self):
        """Create TripLocation Test"""
        url = "/triplocations"
        
        triplocation = {
            "trip_id": 1,
            "location_id": 1
        }
        
        response = self.client.post(url, triplocation, format='json')
        
        new_triplocation = TripLocation.objects.last()
        expected = TripLocationSerializer(new_triplocation)
        self.assertEqual(expected.data, response.data)
    def test_get_triplocation(self):
        """Get TripLocation Test"""
        triplocation = TripLocation.objects.first()
        url = f'/triplocations/{self.triplocation.id}'
        
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        expected = TripLocationSerializer(self.triplocation)
        
        self.assertEqual(expected.data, response.data)
        
    def test_list_triplocations(self):
        """List TripLocations Test"""
        url = "/triplocations"
        
        response = self.client.get(url)
        
        all_triplocations = TripLocation.objects.all()
        expected = TripLocationSerializer(all_triplocations, many=True)
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    
    def test_delete_triplocation(self): 
        """Delete TripLocation Test"""
        triplocation = TripLocation.objects.first()
        url = f'/triplocations/{self.triplocation.id}'
        
        response = self.client.delete(url)
        
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertFalse(TripLocation.objects.filter(pk=self.triplocation.id).exists())
  
