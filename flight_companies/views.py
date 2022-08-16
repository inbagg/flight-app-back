from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .models import Country, Airline_Company, Flight, Ticket
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.db.models import F
from .serializers import ViewCountrySerializer, AirlineCompanySerializer, ViewAirlineCompanySerializer, ViewFlightsSerializer, FlightsSerializer, TicketsSerializer, ViewTicketsSerializer
# Create your views here.


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
@authentication_classes([])
@permission_classes([])
def countries(request, pk=-1):
    if request.method == 'GET':
        try:
            if int(pk) > -1:  # get single product
                countryObj = Country.objects.get(id=pk)
                serializer = ViewCountrySerializer(countryObj, many=False)
            else:
                countries = Country.objects.all()
                # can the 'many' be removed?
                serializer = ViewCountrySerializer(countries, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            countries = Country.objects.all()
            # can the 'many' be removed?
            serializer = ViewCountrySerializer(countries, many=True)
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)
    if request.method == 'POST':
        serializer = ViewCountrySerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})


@api_view(['POST'])
def createCountry(request):
    serializer = ViewCountrySerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})


@api_view(['PUT'])
def updateCountry(request, pk=-1):  # check if exist?
    try:
        country = Country.objects.get(id=pk)
        serializer = ViewCountrySerializer(instance=country, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})


@api_view(['DELETE'])
def deleteCountry(request, pk=-1):  # check if exist?
    try:
        country = Country.objects.get(id=pk)
        country.delete()
        return Response(status=status.HTTP_200_OK, data="country was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def airlineCompanies(request, pk=-1):
    try:
        if int(pk) > -1:  # get single product
            airlineCompanyObj = Airline_Company.objects.get(id=pk)
            serializer = ViewAirlineCompanySerializer(
                airlineCompanyObj, many=False)
        else:
            airlineCompanies = Airline_Company.objects.all()
            serializer = ViewAirlineCompanySerializer(
                airlineCompanies, many=True)  # can the 'many' be removed?
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except:
        airlineCompanies = Airline_Company.objects.all()
        serializer = ViewAirlineCompanySerializer(
            airlineCompanies, many=True)  # can the 'many' be removed?
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def filterFlights(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        origin_Country = data['origin_Country']
        destination_Country = data['destination_Country']
        departure_Time = data['departure_Time']
        landing_Time = data['landing_Time']
        all_data = Flight.objects.all()
        if origin_Country != "":
            all_data = all_data.filter(
                origin_Country=origin_Country)
        if destination_Country != "":
            all_data = all_data.filter(
                destination_Country=destination_Country)
        if departure_Time != "":
            all_data = all_data.filter(
                departure_Time__gte=departure_Time)
        if landing_Time != "":
            all_data = all_data.filter(
                landing_Time__lte=landing_Time)
        all_data = all_data.order_by('-id')
        serializer = ViewFlightsSerializer(
            all_data, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


@api_view(['GET'])
def airlineByOwner(request, pk):
    if request.method == 'GET':
        airlineCompanyObj = Airline_Company.objects.all().filter(user=pk).order_by('-id')
        serializer = ViewAirlineCompanySerializer(
            airlineCompanyObj, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


@api_view(['POST'])
def createAirlineCompany(request):
    serializer = AirlineCompanySerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})


@api_view(['PUT'])
def updateAirlineCompany(request, pk):  # check if exist?
    try:
        airlineCompany = Airline_Company.objects.get(id=pk)
        serializer = AirlineCompanySerializer(
            instance=airlineCompany, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})


@api_view(['DELETE'])
def deleteAirlineCompany(request, pk=-1):  # check if exist?
    try:
        airlineCompany = Airline_Company.objects.get(id=pk)
        airlineCompany.delete()
        return Response(status=status.HTTP_200_OK, data="airline company was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def flights(request, pk=-1):
    try:
        if int(pk) > -1:  # get single product
            flightObj = Flight.objects.get(id=pk)
            serializer = ViewFlightsSerializer(flightObj, many=False)
        else:
            flights = Flight.objects.all()
            # can the 'many' be removed?
            serializer = ViewFlightsSerializer(flights, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except:
        flights = Flight.objects.all()
        # can the 'many' be removed?
        serializer = ViewFlightsSerializer(flights, many=True)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getFlightsOfAirline(request, pk=-1):
    flightObj = Flight.objects.all().filter(
        airline_Company=pk).order_by('-id')
    serializer = ViewFlightsSerializer(flightObj, many=True)
    return Response(status=status.HTTP_200_OK, data=serializer.data)


@api_view(['POST'])
def createFlight(request):
    serializer = FlightsSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})


@api_view(['PUT'])
def updateFlight(request, pk):  # check if exist?
    try:
        flight = Flight.objects.get(id=pk)
        serializer = FlightsSerializer(instance=flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})


@api_view(['DELETE'])
def deleteFlight(request, pk=-1):  # check if exist?
    try:
        flight = Flight.objects.get(id=pk)
        flight.delete()
        return Response(status=status.HTTP_200_OK, data="ticket was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")


@api_view(['GET'])
def tickets(request, pk=-1):
    try:
        if int(pk) > -1:
            customerObj = Ticket.objects.get(id=pk)
            serializer = TicketsSerializer(customerObj, many=False)
        else:
            tickets = Ticket.objects.all()
            serializer = TicketsSerializer(tickets, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except:
        tickets = Ticket.objects.all()
        serializer = TicketsSerializer(tickets, many=True)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)


@api_view(['GET'])
def userTickets(request, pk):
    if request.method == 'GET':
        all_data = Ticket.objects.all().filter(
            customer=pk).order_by('-id')
        serializer = ViewTicketsSerializer(
            all_data, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def createTicket(request):
    data = JSONParser().parse(request)
    try:
        Flight.objects.filter(pk=int(data["flight"])).update(
            remaining_Tickets=F('remaining_Tickets') - int(data["quantity"]))
    except Exception as e:
        print(e)
    serializer = TicketsSerializer(data=data)
    try:
        if serializer.is_valid():  # and flight.remaining_Tickets>0:
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})


@api_view(['PUT'])
def updateTicket(request, pk):
    try:
        ticket = Ticket.objects.get(id=pk)
        serializer = TicketsSerializer(instance=ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})


@api_view(['DELETE'])
def deleteTicket(request, pk=-1):
    try:
        ticket = Ticket.objects.get(id=pk)
        ticket.delete()
        return Response(status=status.HTTP_200_OK, data="ticket was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")


def getRemainingTickets(id=3):
    flight = Flight.objects.get(id=id)
