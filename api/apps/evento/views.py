from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Event
from .serializers import EventSerializer, EventListDateSerializer


class EventViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class EventListDateViewSet(ModelViewSet):
    http_method_names = 'get'
    serializer_class = EventListDateSerializer

    '''Sobre escrevi o método get para que essa url faça o filtro por eventos não Realizados a propriedade 
    ‘eventheld=False’ Para futuro irei criar uma funcionalidade para que essa propriedade seja crida automaticamente'''
    def get_queryset(self):
        return Event.objects.filter(eventheld=False)





