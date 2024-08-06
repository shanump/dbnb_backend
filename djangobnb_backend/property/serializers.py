from rest_framework import serializers
from .models import Property, Reservation

from useraccount.serializers import UserDetailsSerializer

class PropertiesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'price_per_night',
            'image_url',
        )

class PropertiesDetailSerializers(serializers.ModelSerializer):
    landlord = UserDetailsSerializer(read_only=True, many=False)
    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'description',
            'price_per_night',
            'image_url',
            'bedrooms',
            'bathrooms',
            'guests',
            'landlord',
        )

class ReservationsListSerializer(serializers.ModelSerializer):
    property = PropertiesListSerializers(read_only=True, many=False)

    class Meta:
        model= Reservation
        fields = (
            'id', 'start_date', 'end_date', 'number_of_nights', 'total_price', 'property'
        )