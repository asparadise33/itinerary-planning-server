from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from itineraryapi.models import Trip, TravelMode, User, Location

class TripView(ViewSet):
    """Trip Views"""
    def retrieve(self, request, pk):
        """func to get single trip"""
        try:
            trip = Trip.objects.get(pk=pk)
            serializer = TripSerializer(trip)
            return Response(serializer.data)
        except Trip.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """func to list all trips"""
        trips = Trip.objects.all()
        
        destination = request.query_params.get('destination', None)
        if destination is not None:
            trips = trips.filter(destination=destination)
        
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized trip instance
        """

        trip = Trip.objects.create(
            user=request.data["user"],
            destination=request.data["destination"],
            start_date=request.data["start_date"],
            end_date=request.data["end_date"],
            mode_of_travel=request.data["mode_of_travel"],
            number_of_travelers=request.data["number_of_travelers"],
            people_on_trip=request.data["people_on_trip"],
            notes=request.data["notes"]
        )

        serializer = TripSerializer(trip)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a trip

        Returns:
            Response -- Empty body with 204 status code
        """
        trip = Trip.objects.get(pk=pk)
        trip.user = request.data["user"]
        trip.destination = request.data["destination"]
        trip.start_date = request.data["start_date"]
        trip.end_date = request.data["end_date"]
        trip.mode_of_travel = request.data["mode_of_travel"]
        trip.number_of_travelers = request.data["number_of_travelers"]
        trip.people_on_trip = request.data["people_on_trip"]
        trip.notes = request.data["notes"]
        trip.save()
        serializer = TripSerializer(trip)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        trip.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class TravelModeSerializer(serializers.ModelSerializer):
    """JSON serializer for travel modes

    Arguments:
        serializers
    """
    class Meta:
        model = TravelMode
        fields = ('id', 'type_of_travel')
        depth = 1
class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = User
        fields = ("id", "name", "bio", "uid", "created_at")

class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for trips"""
    class Meta:
        model = Trip
        fields = ('id', 'user', 'destination', 'start_date', 'end_date', 'mode_of_travel', 'number_of_travelers', 'people_on_trip', 'notes', 'created_at', 'updated_at')
