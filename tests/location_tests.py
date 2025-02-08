from rest_framework import status
from rest_framework.test import APITestCase
from itineraryapi.models import Location
from itineraryapi.views.location import LocationSerializer

class LocationTests(APITestCase):
  
  fixtures = ['location']
  
  def setUp(self):
    
    self.location = Location.objects.first()
  
  def test_create_location(self):
    """Create Location Test"""
    url = "/locations"
    
    location = {
      "place_name": "test location"
    }
    
    response = self.client.post(url, location, format='json')
    
    new_location = Location.objects.last()
    
    expected = LocationSerializer(new_location)
    
    self.assertEqual(expected.data, response.data)

  def test_get_location(self):
    """Get Location Test"""
    location = Location.objects.first()
    url = f'/locations/{self.location.id}'
    
    response = self.client.get(url)
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    
    expected = LocationSerializer(self.location)
    
    self.assertEqual(expected.data, response.data)
    
  def test_list_locations(self):
    """List Locations Test"""
    url = "/locations"
    
    response = self.client.get(url)
    
    all_locations = Location.objects.all()
    expected = LocationSerializer(all_locations, many=True)
    
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual(expected.data, response.data)

  def test_update_location(self):
    """Update Location Test"""
    location = Location.objects.first()
    url = f'/locations/{self.location.id}'
    
    updated_location = {
      "place_name": f'{self.location.place_name} updated'
    }
    
    response = self.client.put(url, updated_location, format='json')
    
    updated_location = Location.objects.get(pk=self.location.id)
    expected = LocationSerializer(updated_location)
    
    self.assertEqual(expected.data, response.data)
    self.assertEqual(status.HTTP_200_OK, response.status_code)

  def test_delete_location(self):
    """Delete Location Test"""
    location = Location.objects.first()
    url = f'/locations/{self.location.id}'
    
    response = self.client.delete(url)
    
    self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
    
    exists = Location.objects.filter(id=self.location.id).exists()
    
    self.assertFalse(exists)
    response = self.client.get(url)
    self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
