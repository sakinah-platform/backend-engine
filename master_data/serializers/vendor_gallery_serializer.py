from rest_framework import serializers
from master_data.models.vendor_gallery import VendorGallery


class VendorGallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorGallery
        fields = ['uuid', 'id', 'image']
        read_only_fields = ['uuid', 'id', 'image']
