from rest_framework import serializers
from master_data.models.vendor_gallery import VendorGallery


class VendorGallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorGallery
        fields = ['id', 'image']
        read_only_fields = ['id', 'image']
