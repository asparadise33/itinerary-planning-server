from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from itineraryapi.models import TravelMode

class TravelModeView(ViewSet):
    """Travel Mode Views"""

    def retrieve(self, request, pk):
        """func to get single travel mode"""
        try:
            travel_mode = TravelMode.objects.get(pk=pk)
            serializer = TravelModeSerializer(travel_mode)
            return Response(serializer.data)
        except TravelMode.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """func to list all travel modes"""
        travel_modes = TravelMode.objects.all()
        
        type_of_travel = request.query_params.get('type_of_travel', None)
        if type_of_travel is not None:
            travel_modes = travel_modes.filter(type_of_travel=type_of_travel)

        serializer = TravelModeSerializer(travel_modes, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized travel mode instance
        """

        travel_mode = TravelMode.objects.create(
            type_of_travel=request.data["type_of_travel"]
        )

        serializer = TravelModeSerializer(travel_mode)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a travel mode

        Returns:
            Response -- Empty body with 204 status code
        """
        try:
            travel_mode = TravelMode.objects.get(pk=pk)
            travel_mode.type_of_travel = request.data["type_of_travel"]
            travel_mode.save()
            serializer = TravelModeSerializer(travel_mode)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TravelMode.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def destroy(self, request, pk):
        """Handle DELETE requests for a single travel mode

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            travel_mode = TravelMode.objects.get(pk=pk)
            travel_mode.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except TravelMode.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          
class TravelModeSerializer(serializers.ModelSerializer):
    """JSON serializer for travel modes

    Arguments:
        serializers
    """
    class Meta:
        model = TravelMode
        fields = ('id', 'type_of_travel')
        depth = 1
