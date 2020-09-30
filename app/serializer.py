from rest_framework import serializers
from app.models import WeatherAudit


class WeatherAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherAudit
        fields = '__all__'
        