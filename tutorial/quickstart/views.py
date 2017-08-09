from django.shortcuts import render

from django.contrib.auth.models import User, Group
from .models import UserTest, Entry
from rest_framework import viewsets
from .serializers import UserSerializers, GroupSerializers, UserTestSerializers, EntrySerializers


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
       API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers


class GroupViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializers


class UserTestViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows UserTest to be viewed or edited.
    """
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializers


class EntryViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows Entry to be viewed or edited.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializers
