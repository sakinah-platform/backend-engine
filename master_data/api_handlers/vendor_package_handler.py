from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.db import models
from django_filters import rest_framework as filters

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import NotFound

from backend.system_utility.custom_search_utility import CustomSearchFilter
from backend.system_utility.pagination_utility import FiftyResultsPagination
from backend.system_utility.settings_utility import DEFAULT_CACHE_TIME

from master_data.models.vendor_package import VendorPackage
from master_data.models.vendor import Vendor
from master_data.serializers.vendor_package_serializer import VendorPackageSerializer, VendorPackageListSerializer


class VendorPackageFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = VendorPackage
        fields = ['short_descriptions']
        filter_overrides = {
            models.JSONField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }


@method_decorator(cache_page(DEFAULT_CACHE_TIME), name='list')
class VendorPackageViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):

    queryset = VendorPackage.objects.all()
    pagination_class = FiftyResultsPagination
    filter_backends = [filters.DjangoFilterBackend, CustomSearchFilter]
    filterset_class = VendorPackageFilter
    ordering_fields = ('name', 'created_at')
    ordering = ('-name',)
    search_fields = ['name']

    def get_queryset(self, *args, **kwargs):
        vendor_id = self.kwargs.get("vendor_pk")
        try:
            vendor = Vendor.objects.get(uuid=vendor_id)
        except Vendor.DoesNotExist:
            raise NotFound('A vendor with this id does not exist.')

        return self.queryset.filter(vendor=vendor)

    def get_serializer_class(self):
        if self.action in ['list']:

            return VendorPackageListSerializer

        return VendorPackageSerializer
