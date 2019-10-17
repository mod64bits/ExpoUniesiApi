from django.db import models

from apps.evento.models import Attraction
from django.contrib.auth.models import User



class VisitorType(models.Model):
    VISITOR_TYPE_CHOICES = [
        ('ALUNO', 'Aluno'),
        ('PROFESSOR', 'Professor'),
        ('CONVIDADO', 'Convidado'),
    ]
    EVENT_AD = [
        ('WEBSITE', 'Website'),
        ('AMIGO', 'Amigo'),
        ('SOCIAL', 'Redes Sociais'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario Logado', null=True, blank=True)
    visitorName = models.CharField('Nome Completo', max_length=100)
    visitorPhone = models.CharField('Telefone', max_length=30)
    visitorEmail = models.EmailField('Seu Email', null=True, blank=True)
    visitorType = models.CharField('Tipo de Visitante', max_length=10, choices=VISITOR_TYPE_CHOICES)
    event = models.ForeignKey(Attraction, on_delete=models.CASCADE)

    ad = models.CharField('Como ouviu falar do evento', max_length=10, choices=EVENT_AD)
    feedback = models.TextField('Comentários e ou perguntas')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.visitorName

