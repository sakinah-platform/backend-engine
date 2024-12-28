from rest_framework import serializers
from master_data.models.vendor_package import VendorPackage

from master_data.serializers.package_gallery_serializer import PackageGallerySerializer


class VendorPackageListSerializer(serializers.ModelSerializer):
    first_image = PackageGallerySerializer(read_only=True)

    class Meta:
        model = VendorPackage
        fields = ['id', 'name', 'price', 'description', 'first_image']
        read_only_fields = ['id', 'name', 'price', 'description']


class VendorPackageSerializer(VendorPackageListSerializer):

    galleries = PackageGallerySerializer(many=True, read_only=True)
    price = serializers.IntegerField()

    class Meta:
        model = VendorPackage
        fields = ['id', 'name', 'price', 'terms_and_condition', 'description', 'galleries']
        read_only_fields = ['id', 'name', 'price', 'terms_and_condition', 'description', 'galleries']
