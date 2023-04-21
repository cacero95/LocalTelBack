from rest_framework import routers
from .viewsets import CustomUserViewSet, AccountViewset
from django.urls import path
from  . import views

urlpatterns = [
    path( 'user/login', views.login ),
    path( 'user/register', views.Register ),
    path( 'account/getAccount', views.getAccountByEmail ),
    path( 'account/addFounds', views.addFounds ),
    path( 'account/takeOutAmount', views.takeOutAmount )
]

route = routers.SimpleRouter()
route.register( 'account', AccountViewset )
route.register( 'user', CustomUserViewSet )
urlpatterns += route.urls
