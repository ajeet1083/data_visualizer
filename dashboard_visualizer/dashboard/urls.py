from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataPointViewSet

router = DefaultRouter()
router.register(r'datapoints', DataPointViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
