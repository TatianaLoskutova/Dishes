from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FoodViewSet

app_name = 'api'

router = DefaultRouter()

router.register('foods', FoodViewSet)

urlpatterns = (
    path('', include(router.urls)),
)
