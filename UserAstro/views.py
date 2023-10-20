from UserAstro.Serializers import NatalFirstTimeSerializer,UserRegistrationSerializer,UserSettingSerializer
from .models import *
from rest_framework.response import Response
from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny



class NatalFirstTimeViewSet(viewsets.ModelViewSet):
    queryset = Natal_First_Time_Table.objects.all()
    serializer_class = NatalFirstTimeSerializer
    permission_classes = (AllowAny,)
    
class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User_Registration_Table.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
    
class UserSettingViewSet(viewsets.ModelViewSet):

    queryset = User_Setting_Table.objects.all()
    serializer_class = UserSettingSerializer
    permission_classes = (AllowAny,)     