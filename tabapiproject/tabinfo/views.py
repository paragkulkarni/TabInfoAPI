from django.shortcuts import render
from django.contrib.auth.models import User

from .serializers import TabinfoSerializer,UserSerializer
from .models import Tabinfo
from .permissions import IsOwnerOrReadOnly


from rest_framework import generics,permissions



class TabinfoViewSet(generics.ListAPIView):
    queryset = Tabinfo.objects.all()
    serializer_class = TabinfoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
