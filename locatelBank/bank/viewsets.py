from rest_framework import viewsets
from .models import Account, CustomUser
from .serializers import AccountSerializer, CustomUserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class AccountViewset( viewsets.ModelViewSet ):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class CustomUserViewSet( viewsets.ModelViewSet ):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @action( detail = True, methods = ['GET'] )
    def login( self, request ):
        try:
            print( self )
            print( request )
            return Response({ "ok" : True, "message" : "" })
        except:
            print( 'error' )
            return Response({ "ok" : False, "message" : "" })