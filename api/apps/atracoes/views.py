from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Attraction
from .serializers import AttractionSerializer
from rest_framework.viewsets import ModelViewSet

class AttractionViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

