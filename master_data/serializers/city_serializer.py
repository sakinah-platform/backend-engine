from rest_framework import serializers

from backend.system_utility.settings_utility import string_for_datetime
from master_data.models.city import City


class CityListSerializer(serializers.ModelSerializer):

    name = serializers.CharField(read_only=True)

    class Meta:
        model = City
        fields = ('id', 'name')


class CityReadSerializer(CityListSerializer):

    description = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, format=string_for_datetime())

    class Meta:
        model = City
        fields = ('id', 'name', 'description', 'created_at')
