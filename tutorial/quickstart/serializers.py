from django.contrib.auth.models import User, Group
from .models import UserTest, Entry
from rest_framework import serializers

# Serializer是将「Model序列化」

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UserTestSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserTest
        fields = ('name', 'mail')

class EntrySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')
