from rest_framework import serializers
from .models import Account, CustomUser
from rest_framework.response import Response

class CustomUserSerializer( serializers.ModelSerializer ):

    class Meta:
        model = CustomUser
        fields = ( 'name', 'last_name', 'email', 'email', 'password' )

    
class AccountSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Account
        fields = ( 'number', 'amount', 'user', 'created_at', 'updated_at' )
