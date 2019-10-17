from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Event
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from datetime import date as dateserver
from apps.atracoes.serializers import AttractionSerializer


#CURRENTDATE = dateserver.today()


class EventSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    attraction = AttractionSerializer(many=True)

    class Meta:
        model = Event
        fields = ['id', 'owner', 'name', 'place', 'date', 'place', 'description', 'attraction', 'created', 'modified',
                  'eventheld']


class EventListDateSerializer(ModelSerializer):
    attraction = AttractionSerializer(many=True)
    class Meta:
        model = Event
        fields = ['id', 'name', 'place', 'date', 'place', 'description', 'attraction', 'eventheld']

















