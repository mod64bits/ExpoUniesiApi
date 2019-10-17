from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.visitantes.models import VisitorType


class VisitsReportSerializer(ModelSerializer):

    class Meta:
        model = VisitorType
        fields = ['visitorName']


