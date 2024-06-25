from rest_framework import serializers
from .models import DataEntry

class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataEntry
        fields = '__all__'
