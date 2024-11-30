from rest_framework import serializers
from master_data.models.vendor_package import VendorPackage


class VendorPackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorPackage
        fields = ['id', 'name', 'price', 'description']
        read_only_fields = ['id', 'name', 'price', 'description']
