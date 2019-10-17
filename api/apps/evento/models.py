from django.db import models
from django.contrib.auth.models import User
from apps.atracoes.models import Attraction

class Event(models.Model):
    name = models.CharField('Nome do Evento', max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name='Dono do Evento', null=True, blank=True)
    date = models.DateField('Data')
    schedule = models.TimeField('Horario')
    place = models.CharField('Local do evnto', max_length=100)
    description = models.TextField('Descrição', null=True, blank=True)
    attraction = models.ManyToManyField(Attraction, verbose_name='Atrações')
    eventheld = models.BooleanField('Evento Realizado', default=False)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name





