from rest_framework import serializers
from master_data.models.vendor import Vendor

from master_data.serializers.vendor_gallery_serializer import VendorGallerySerializer
from master_data.serializers.vendor_package_serializer import VendorPackageSerializer
from master_data.serializers.vendor_schedule_serializer import VendorScheduleSerializer


class VendorSerializer(serializers.ModelSerializer):
    galleries = VendorGallerySerializer(many=True, read_only=True)
    packages = VendorPackageSerializer(many=True, read_only=True)
    schedules = VendorScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = ['id',
                  'name',
                  'description',
                  'about',
                  'category',
                  'email',
                  'facebook',
                  'instagram',
                  'tiktok',
                  'youtube',
                  'profile_image',
                  'availability',
                  'visibility',
                  'galleries',
                  'packages',
                  'schedules']
        read_only_fields = ['id',
                            'name',
                            'description',
                            'about',
                            'category',
                            'email',
                            'facebook',
                            'instagram',
                            'tiktok',
                            'youtube',
                            'profile_image',
                            'availability',
                            'visibility']
