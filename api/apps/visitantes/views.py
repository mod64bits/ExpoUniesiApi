from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import VisitorType
from .serializers import VisitorSerializer

class VisitorViewSet(ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated, ]
    queryset = VisitorType.objects.all()
    serializer_class = VisitorSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

