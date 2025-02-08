from rest_framework import status
from rest_framework.test import APITestCase
from itineraryapi.models import Location, Trip, TripLocation
# TODO: DOESN'T WORK
class TripLocationTests(APITestCase):
    fixtures = ['location', 'trip', 'triplocation']
    def setUp(self):
        self.triplocation = TripLocation.objects.first()
    
    def test_create_triplocation(self):
        """Create TripLocation Test"""
        url = "/triplocations"
        
        triplocation = {
            "trip": 1,
            "location": 1
        }
        
        response = self.client.post(url, triplocation, format='json')
        
        new_triplocation = TripLocation.objects.last()
        
        self.assertEqual(new_triplocation.trip_id, response.data['trip'])
        self.assertEqual(new_triplocation.location_id, response.data['location'])
    
    def test_get_triplocation(self):
        """Get TripLocation Test"""
        triplocation = TripLocation.objects.first()
        url = f'/triplocations/{self.triplocation.id}'
        
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        self.assertEqual(self.triplocation.trip_id, response.data['trip'])
        self.assertEqual(self.triplocation.location_id, response.data['location'])
    
    def test_list_triplocations(self):
        """List TripLocations Test"""
        url = "/triplocations"
        
        response = self.client.get(url)
        
        all_triplocations = TripLocation.objects.all()
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(all_triplocations), len(response.data))
    
    def test_delete_triplocation(self):
        """Delete TripLocation Test"""
        triplocation = TripLocation.objects.first()
        url = f'/triplocations/{self.triplocation.id}'
        
        response = self.client.delete(url)
        
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        
        self.assertFalse(TripLocation.objects.filter(id=self.triplocation.id).exists())
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

        
        
