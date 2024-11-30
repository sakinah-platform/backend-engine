from rest_framework import serializers
from master_data.models.vendor_schedule import VendorSchedule


class VendorScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorSchedule
        fields = ['day', 'start_time', 'end_time']
        read_only_fields = ['day', 'start_time', 'end_time']
