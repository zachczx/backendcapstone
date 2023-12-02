from rest_framework import serializers
from .models import *
from decimal import Decimal

class MenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Menu
        fields = "__all__"
        
class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = "__all__"
