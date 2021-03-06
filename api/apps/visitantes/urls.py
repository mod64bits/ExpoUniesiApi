from django.urls import include, path
from rest_framework import routers
from apps.user import views
from .views import VisitorViewSet

router = routers.DefaultRouter()
router.register('', VisitorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),

]

