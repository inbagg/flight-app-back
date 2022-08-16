from django.db import models
from customers.models import Customer

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name


class Airline_Company(models.Model):
    name = models.CharField(max_length=20, unique=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Airline Companies"

    def __str__(self):
        return self.name


class Flight(models.Model):
    airline_Company = models.ForeignKey(
        Airline_Company, on_delete=models.SET_NULL, null=True)
    destination_Country = models.ForeignKey(
        Country, related_name='flight_destanation', on_delete=models.SET_NULL, null=True)
    origin_Country = models.ForeignKey(
        Country, related_name='flight_origin', on_delete=models.SET_NULL, null=True)
    departure_Time = models.DateTimeField(null=True)
    landing_Time = models.DateTimeField(null=True)
    remaining_Tickets = models.IntegerField()
    price = models.IntegerField()
    image = models.TextField(null=True, default="", blank=True)

    def __str__(self):
        return (f"{self.airline_Company} to {self.destination_Country}")


class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return (f"flight: {self.flight} customer: {self.customer}")
