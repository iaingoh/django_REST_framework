from rest_framework import serializers
from .models import JsonDataPoint


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = JsonDataPoint
        fields = '__all__'