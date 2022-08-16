from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializers
from . import models


# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['role'] = self.user.role
        data['address'] = self.user.address
        data['phone_no'] = self.user.phone_no
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomerCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = serializers.CustomerSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                pass
            except:
                return JsonResponse({'message': "Username is already used!"}, status=status.HTTP_200_OK)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse({'message': serializer.errors}, status=status.HTTP_200_OK)

    def get(self, request):
        users = models.Customer.objects.all()
        users_serializer = serializers.ViewCustomerSerializer(
            users, many=True)
        return JsonResponse(users_serializer.data, safe=False)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)


@api_view(['GET'])
def users(request, pk=-1):
    try:
        if int(pk) > -1:
            userObj = User.objects.get(id=pk)
            serializer = serializers.ViewCustomerSerializer(
                userObj, many=False)
        else:
            users = User.objects.all()
            serializer = serializers.ViewCustomerSerializer(users, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except:
        users = User.objects.all()
        serializer = serializers.ViewCustomerSerializer(users, many=True)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def customers(request, pk=-1):
    try:  # method get all
        if int(pk) > -1:  # get single product
            customerObj = models.Customer.objects.get(id=pk)
            serializer = serializers.ViewCustomerSerializer(
                customerObj, many=False)
        else:
            customers = models.Customer.objects.all()
            serializer = serializers.ViewCustomerSerializer(
                customers, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except:
        customers = models.Customer.objects.all()
        serializer = serializers.ViewCustomerSerializer(customers, many=True)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)


@api_view(['POST', 'GET'])
def createCustomer(request):
    if request == 'POST':
        # with transaction.atomic():
        try:
            userSerializer = serializers.ViewCustomerSerializer(
                data=request.data)
            print("did we get here?                       .")
            print(userSerializer.data)
            if userSerializer.is_valid():
                try:
                    userSerializer.save()
                except IntegrityError as ex:
                    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data=ex)
                user = User.objects.get(email=userSerializer.data["email"])
                customerSerializer = serializers.CustomerSerializer(
                    instance=user, data=request.data)
                if customerSerializer.is_valid():
                    customer = customerSerializer.save()
                    return Response(status=status.HTTP_200_OK, data=customerSerializer.data)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data=customerSerializer.errors)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})
    else:
        customers = models.Customer.objects.all()
        serializer = serializers.ViewCustomerSerializer(customers, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


@api_view(['PUT'])
def updateCustomer(request, pk):  # check if exist?
    try:
        customer = models.Customer.objects.get(id=pk)
        serializer = serializers.CustomerSerializer(
            instance=customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")


@api_view(['DELETE'])
def deleteCustomer(request, pk):  # check if exist?
    try:
        customer = models.Customer.objects.get(id=pk)
        customer.delete()
        return Response(status=status.HTTP_200_OK, data="customer was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")
