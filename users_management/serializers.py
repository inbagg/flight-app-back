from rest_framework import serializers
from .models import User_Role, Administrator

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Role
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = '__all__'