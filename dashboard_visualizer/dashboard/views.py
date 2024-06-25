from rest_framework import viewsets
from .models import DataEntry
from .serializers import DataPointSerializer

class DataPointViewSet(viewsets.ModelViewSet):
    queryset = DataEntry.objects.all()
    serializer_class = DataPointSerializer
