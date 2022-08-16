from django.contrib import admin
from .models import Country, Airline_Company, Flight, Ticket

admin.site.register(Country)
admin.site.register(Airline_Company)
admin.site.register(Flight)
admin.site.register(Ticket)
