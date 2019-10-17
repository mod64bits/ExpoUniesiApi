"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.evento.views import EventListDateViewSet
from apps.relatorios.views import VisitsReportSerializer
from apps.visitantes import urls as visitantes_url
from apps.atracoes import urls as atracoes_urls
from apps.relatorios import urls as relatorios_url
from apps.user import urls as user_url
from rest_framework.authtoken.views import obtain_auth_token

from apps.evento import urls as evento_url

router = routers.DefaultRouter()
#router.register('relatorios', VisitsReportSerializer)
router.register('listaeventos', EventListDateViewSet, base_name='Event')

urlpatterns = [
    path('', include(router.urls)),
    path('relatorios/', include(relatorios_url)),
    path('reserva/', include(visitantes_url)),
    path('atracoes/', include(atracoes_urls)),
    path('eventos/', include(evento_url)),
    path('api-token-auth/', obtain_auth_token),
    path('user/', include(user_url)),
    #path('api/', include(router.urls)),
    path('admin/', admin.site.urls),

]
