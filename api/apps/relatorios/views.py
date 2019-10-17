from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.visitantes.models import VisitorType
from .serializers import VisitsReportSerializer


class TotalDeVisitaViewSet(ModelViewSet):

    serializer_class = VisitsReportSerializer

    def get_queryset(self):
        return VisitorType.objects.all()

    def list(self, request, *args, **kwargs):
        visitantes = VisitorType.objects.all()
        total = visitantes.count()
        alunos = visitantes.filter(visitorType="ALUNO").count()
        professor = visitantes.filter(visitorType="PROFESSOR").count()
        convidado = visitantes.filter(visitorType="CONVIDADO").count()
        return Response({
            'Total Visitantes': total,
            'Total de Alunos': alunos,
            'Total de Professores': professor,
            'Total de Convidados': convidado,
        })