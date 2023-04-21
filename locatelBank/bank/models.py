from django.db import models

# Create your models here.

class CustomUser( models.Model ):

    name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    password = models.TextField()

class Account( models.Model ):

    number = models.IntegerField()
    amount = models.IntegerField()
    user = models.ForeignKey( CustomUser, null = False, on_delete = models.CASCADE )
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )
