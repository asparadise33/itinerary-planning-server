from rest_framework import status
from rest_framework.test import APITestCase

from itineraryapi.models import TravelMode
from itineraryapi.views.travelmode import TravelModeSerializer

class TravelModeTests(APITestCase):
    # fixtures for travel mode
    fixtures = ['mode']
    def setUp(self):
        # grab first travel mode from db
        self.travelmode = TravelMode.objects.first()
    
    def test_create_travelmode(self):
        """Create TravelMode Test"""
        url = "/travelmodes"
        # Define travel mode properties
        travelmode = {
            "type_of_travel": "automobile"
            
        }
        
        response = self.client.post(url, travelmode, format='json')
        
        new_travelmode = TravelMode.objects.last()
        
        expected = TravelModeSerializer(new_travelmode)
        self.assertEqual(expected.data, response.data)
    
    def test_get_travelmode(self):
        """Get TravelMode Test"""
        travelmode = TravelMode.objects.first()
        url = f'/travelmodes/{self.travelmode.id}'
        
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        expected = TravelModeSerializer(self.travelmode)
        
        self.assertEqual(expected.data, response.data)
    
    def test_list_travelmodes(self):
        """List TravelModes Test"""
        url = "/travelmodes"
        
        response = self.client.get(url)
        
        all_travelmodes = TravelMode.objects.all()
        expected = TravelModeSerializer(all_travelmodes, many=True)
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)

    def test_update_travelmode(self):
        """Update TravelMode Test"""
        travelmode = TravelMode.objects.first()
        url = f'/travelmodes/{self.travelmode.id}'
        
        updated_travelmode = {
            "type_of_travel": f'{self.travelmode.type_of_travel} updated'
        }
        
        response = self.client.put(url, updated_travelmode, format='json')
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        travelmode.refresh_from_db()
        
        self.assertEqual(updated_travelmode['type_of_travel'], travelmode.type_of_travel)

    def test_delete_travelmode(self):
        """Delete TravelMode Test"""
        travelmode = TravelMode.objects.first()
        url = f'/travelmodes/{self.travelmode.id}'
        
        response = self.client.delete(url)
        
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        
        exists = TravelMode.objects.filter(id=self.travelmode.id).exists()
        
        self.assertFalse(exists)
        
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
