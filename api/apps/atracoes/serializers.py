from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Attraction
from rest_framework import viewsets

class AttractionSerializer(ModelSerializer):
    class Meta:
        model = Attraction
        fields = ['id', 'name', 'description', 'created', 'modified']


