from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from itineraryapi.models import Location

class LocationView(ViewSet):

  """ Location Views
  """
  def retrieve(self, request, pk):
    """get a single location function
    """
    try:
      location=Location.objects.get(pk=pk)
      serializer = LocationSerializer(location)
      return Response(serializer.data)
    except Location.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
  
    
  def list(self, request):
    """Gets Locations
    """
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)
    
  def create(self, request):
    """Create a Location Function
        """

    location = Location.objects.create(
     place_name=request.data["place_name"],
        )
    serializer = LocationSerializer(location)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
  def update(self, request, pk):
    """Update Function for Location
        """
    location = Location.objects.get(pk=pk)
    location.place_name=request.data["place_name"]
    location.save()
    serializer = LocationSerializer(location)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
  def destroy(self, request, pk):
      location = Location.objects.get(pk=pk)
      location.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)


class LocationSerializer(serializers.ModelSerializer):
    """JSON serializer for locations
    """
    class Meta:
        model = Location
        fields = ('id', 'place_name')
        
