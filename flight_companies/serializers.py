from rest_framework import serializers
from .models import Country, Airline_Company, Flight, Ticket
from customers.serializers import ViewCustomerSerializer


class ViewCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class AirlineCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline_Company
        fields = '__all__'


class ViewAirlineCompanySerializer(serializers.ModelSerializer):
    country = ViewCountrySerializer()
    user = ViewCustomerSerializer()

    class Meta:
        model = Airline_Company
        fields = '__all__'


class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class ViewFlightsSerializer(serializers.ModelSerializer):
    airline_Company = AirlineCompanySerializer()
    origin_Country = ViewCountrySerializer()
    destination_Country = ViewCountrySerializer()

    class Meta:
        model = Flight
        fields = '__all__'


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class ViewTicketsSerializer(serializers.ModelSerializer):
    flight = ViewFlightsSerializer()
    customer = ViewCustomerSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'
