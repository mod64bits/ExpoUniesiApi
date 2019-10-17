from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import VisitorType
from rest_framework import viewsets
from apps.evento.serializers import EventListDateSerializer

class VisitorSerializer(ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    #event = EventListDateSerializer(many=True)
    class Meta:
        model = VisitorType
        fields = ['id', 'user', 'visitorName', 'visitorPhone',  'visitorEmail', 'visitorType', 'event', 'feedback',
                  'modified', 'created']
