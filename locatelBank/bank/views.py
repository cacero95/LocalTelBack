from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import CustomUser, Account
import json
from django.core import serializers

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def login( request ):
    try:
        body = json.loads( request.body )
        user = CustomUser.objects.get( email = body['email'], password = body['password'] )
        return Response({
            'status'    : True,
            "id"        : user.id,
            "email"     : user.email,
            "name"      : user.name,
            "last_name" : user.last_name,
        })
    except CustomUser.DoesNotExist:
        return Response({ "status" : False, 'message': 'user was not found' })

@api_view(['POST'])
@permission_classes([AllowAny])
def Register( request ):
    try:
        body = json.loads( request.body )
        user = CustomUser(
            name = body[ "name" ],
            last_name = body[ "name" ],
            email = body[ "email" ],
            password = body[ "password" ]
        )
        user.save()
        return Response({
            'status'    : True,
            "id"        : user.id,
            "email"     : user.email,
            "name"      : user.name,
            "last_name" : user.last_name
        })
    except:
        return Response({ "status" : False, "message" : "error" })
    
@api_view(['POST'])
@permission_classes([AllowAny])
def getAccountByEmail( request ):
    try:
        body = json.loads( request.body )
        user = CustomUser.objects.get( email = body['email'] )
        print( user )
        if user is not None:
            accounts = Account.objects.all().filter(
                user_id = user.id
            )
            if len( accounts ) > 0:
                return Response({
                    "status" : True,
                    "message" : "",
                    "accounts" : map (
                        lambda account: {
                            "number": account.number,
                            "amount": account.amount
                        },
                        accounts
                    )
                })
            return Response({ "status": False, "message": "account was not found" })
        
        return Response({ "status" : False, "message" : "Notfound" })
    except:
        return Response({ "status" : False, "message" : "error" })

@api_view(['PUT'])
@permission_classes([AllowAny])
def addFounds( request ):
    try:
        body = json.loads( request.body )
        account = Account.objects.get( number = body[ 'number' ] )
        if account is not None:
            account.amount = account.amount + body[ "amount" ]
            return { "status" : True, "message" : '' }
        return Response({ "status" : False, "message" : 'Account waas not found' })
    except Account.DoesNotExist:
        return Response({ "status" : False, "message" : "error" })

@api_view(['PUT'])
@permission_classes([AllowAny])
def takeOutAmount( request ):
    try:
        body = json.loads( request.body )
        account = Account.objects.get( number = body[ 'number' ] )
        if account is not None:
            account.amount = account.amount - body[ "amount" ]
            return { "status" : True, "message" : '' }
    except Account.DoesNotExist:
        return Response({ "status" : False, "message" : "error" })
