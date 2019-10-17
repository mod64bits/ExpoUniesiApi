from django.db import models


class Attraction(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name