from django.shortcuts import render

from .serializers import TabinfoSerializer
from .models import Tabinfo

from rest_framework import viewsets


class TabinfoViewSet(viewsets.ModelViewSet):
    queryset = Tabinfo.objects.all()
    serializer_class = TabinfoSerializer
