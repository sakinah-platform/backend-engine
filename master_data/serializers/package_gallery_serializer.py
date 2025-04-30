from rest_framework import serializers
from master_data.models.package_gallery import PackageGallery


class PackageGallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = PackageGallery
        fields = ['uuid', 'id', 'image']
        read_only_fields = ['uuid', 'id', 'image']
