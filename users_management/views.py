from .models import User_Role, Administrator
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def roles(request,pk=-1):
    try:
        if int(pk) > -1:    #get single product
            roleObj = User_Role.objects.get(id=pk)
            serializer = RolesSerializer(roleObj, many=False)
        else:
            roles = User_Role.objects.all()
            serializer = RolesSerializer(roles, many=True)   ################can the 'many' be removed?
        return Response(status=status.HTTP_200_OK ,data=serializer.data)
    except:
        roles = User_Role.objects.all()
        serializer = RolesSerializer(roles, many=True)   ################can the 'many' be removed?
        return Response(status=status.HTTP_400_BAD_REQUEST ,data=serializer.data)

@api_view(['POST'])
def createRole(request):
    serializer = RolesSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})

@api_view(['PUT'])
def updateRole(request,pk=-1):  #check if exist?
    try:
        role = User_Role.objects.get(id=pk)
        serializer = RolesSerializer(instance=role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})

@api_view(['DELETE'])
def deleteRole(request,pk=-1):  #check if exist?
    try:
        role = User_Role.objects.get(id=pk)
        role.delete()
        return Response(status=status.HTTP_200_OK, data="role was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def administrators(request,pk=-1):
    try:
        if int(pk) > -1:    #get single product
            administratorObj = Administrator.objects.get(id=pk)
            serializer = AdminSerializer(administratorObj, many=False)
        else:
            administrators = Administrator.objects.all()
            serializer = AdminSerializer(administrators, many=True)   ################can the 'many' be removed?
        return Response(status=status.HTTP_200_OK ,data=serializer.data)
    except:
        administrators = Administrator.objects.all()
        serializer = AdminSerializer(administrators, many=True)
        return Response(status=status.HTTP_400_BAD_REQUEST ,data=serializer.data)

@api_view(['POST'])
def createAdministrator(request):
    serializer = AdminSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})

@api_view(['PUT'])
def updateAdministrator(request,pk=-1):  #check if exist?
    try:
        administrator = Administrator.objects.get(id=pk)
        serializer = AdminSerializer(instance=administrator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data= {"message": ex})

@api_view(['DELETE'])
def deleteAdministrator(request,pk=-1):  #check if exist?
    try:
        administrator = Administrator.objects.get(id=pk)
        administrator.delete()
        return Response(status=status.HTTP_200_OK, data="administrator was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")


