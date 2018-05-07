from django.shortcuts import render
from django.contrib.auth.models import User

from .serializers import TabinfoSerializer,UserSerializer
from .models import Tabinfo

from rest_framework import generics


class TabinfoViewSet(generics.ListAPIView):
    queryset = Tabinfo.objects.all()
    serializer_class = TabinfoSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
