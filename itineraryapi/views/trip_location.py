from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from itineraryapi.models import TripLocation, Trip, Location

class TripLocationView(ViewSet):
    """Trip Location Views"""

    def retrieve(self, request, pk):
        """func to get single trip location"""
        try:
            trip_location = TripLocation.objects.get(pk=pk)
            serializer = TripLocationSerializer(trip_location)
            return Response(serializer.data)
        except TripLocation.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """func to list all trip locations"""
        trip_locations = TripLocation.objects.all()
        
        trip_id = request.query_params.get('trip_id', None)
        if trip_id is not None:
            trip_locations = trip_locations.filter(trip_id=trip_id)

        serializer = TripLocationSerializer(trip_locations, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized trip location instance
        """


        tripLocation = TripLocation.objects.create(
            trip= Trip.objects.get(pk=request.data["trip_id"]),
            location = Location.objects.get(pk=request.data["location_id"])
        )

        serializer = TripLocationSerializer(tripLocation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

 
    def destroy(self, request, pk):
        """Handle DELETE requests for a single trip location

        Returns:
            Response -- 204, 404, or 500 status code
        """
        try:
            trip_location = TripLocation.objects.get(pk=pk)
            trip_location.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except TripLocation.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class TripLocationSerializer(serializers.ModelSerializer): 
    class Meta:
        model = TripLocation
        fields = ('id', 'trip', 'location')
        depth = 1
