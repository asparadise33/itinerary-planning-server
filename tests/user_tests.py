from rest_framework import status
from rest_framework.test import APITestCase

from itineraryapi.models import User
from itineraryapi.views.user import UserSerializer

class UserTests(APITestCase):
    
    fixtures = ['user']
    def setUp(self):
      
        self.user = User.objects.first()
    
    def test_create_user(self):
        """Create User Test"""
        url = "/users"
        
        user = {
            "name": "testuser",
            "bio": "test bio",
            "uid": "{whatevs}"
            
        }
        
        response = self.client.post(url, user, format='json')

        new_user = User.objects.last()
        
        expected = UserSerializer(new_user)
        # Now we can test that the expected ouput matches what was actually returned
        # The _expected_ output should come first when using an assertion with 2 arguments
        # The _actual_ output will be the second argument
        self.assertEqual(expected.data, response.data)

    def test_get_user(self):
        """Get User Test"""
        user = User.objects.first()
        url = f'/users/{self.user.uid}'
        
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        expected = UserSerializer(self.user)
        
        self.assertEqual(expected.data, response.data)
        
    def test_list_users(self):
        """List Users Test"""
        url = "/users"
        
        response = self.client.get(url)
        
        all_users = User.objects.all()
        expected = UserSerializer(all_users, many=True)
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    def test_update_user(self):
        """Update User Test"""
        user = User.objects.first()
        url = f'/users/{self.user.id}'
        
        updated_user = {
            "name": f'{user.name} updated',
            "bio": user.bio,
            "uid": "{whatevs}"
        }
        
        response = self.client.put(url, updated_user, format='json')
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        user.refresh_from_db()
        
        self.assertEqual(updated_user['name'], user.name)
    def test_delete_user(self):
        """Delete User Test"""
        user = User.objects.first()
        url = f'/users/{self.user.id}'
        
        response = self.client.delete(url)
        
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        
        exists = User.objects.filter(id=self.user.id).exists()
        
        self.assertFalse(exists)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
