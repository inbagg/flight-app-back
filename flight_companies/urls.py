from django.urls import path, include
from . import views

urlpatterns = [
    path('flight_companies/', views.airlineCompanies),
    path('countries/', views.countries, name="countries"),
    path('countries/<str:pk>/', views.countries, name="countries"),
    path('create-country/', views.createCountry, name='create-country'),
    path('update-country/<str:pk>/', views.updateCountry, name='update-country'),
    path('delete-country/<str:pk>/', views.deleteCountry, name='delete-country'),

    path('airline-companies/', views.airlineCompanies, name="airline-companies"),
    path('airline-companies/<str:pk>/',
         views.airlineCompanies, name="airline-companies"),
    path('airline-owner/<str:pk>/',
         views.airlineByOwner, name="airline-owner"),
    path('create-airline-company/', views.createAirlineCompany,
         name='create-airline-company'),
    path('update-airline-company/<str:pk>/',
         views.updateAirlineCompany, name='update-airline-company'),
    path('delete-airline-company/<str:pk>/',
         views.deleteAirlineCompany, name='delete-airline-company'),

    path('flights/', views.flights, name="flights"),
    path('filter-flights/', views.filterFlights, name="filter flights"),
    path('flights-by-airline-id/<str:pk>/',
         views.getFlightsOfAirline, name="flights by airline"),
    path('flights/<str:pk>/', views.flights, name="flights"),
    path('create-flight/', views.createFlight, name='create-flight'),
    path('update-flight/<str:pk>/', views.updateFlight, name='update-flight'),
    path('delete-flight/<str:pk>/', views.deleteFlight, name='delete-flight'),

    path('tickets/', views.tickets, name="tickets"),
    path('tickets-by-user/<str:pk>/', views.userTickets, name="tickets"),
    path('tickets/<str:pk>/', views.tickets, name="tickets"),
    path('create-ticket/', views.createTicket, name='create-ticket'),
    path('update-ticket/<str:pk>/', views.updateTicket, name='update-ticket'),
    path('delete-ticket/<str:pk>/', views.deleteTicket, name='delete-ticket'),
]
