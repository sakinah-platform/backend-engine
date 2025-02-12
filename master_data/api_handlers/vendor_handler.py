from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.db.models import Min
from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from backend.system_utility.custom_search_utility import CustomSearchFilter
from backend.system_utility.pagination_utility import FiftyResultsPagination
from backend.system_utility.settings_utility import DEFAULT_CACHE_TIME

from master_data.models.vendor import Vendor
from master_data.serializers.vendor_serializer import VendorSerializer, VendorListSerializer


class VendorFilter(filters.FilterSet):
    starting_price = filters.NumberFilter(field_name='packages__price', lookup_expr='gte')

    class Meta:
        model = Vendor
        fields = {
            'category': ['exact'],
            'city': ['exact']
        }


@method_decorator(cache_page(DEFAULT_CACHE_TIME), name='list')
class VendorViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):

    queryset = Vendor.objects.all().annotate(starting_price=Min('packages__price'))
    pagination_class = FiftyResultsPagination
    filter_backends = [filters.DjangoFilterBackend, CustomSearchFilter]
    filterset_class = VendorFilter
    ordering_fields = ('id', 'name', 'created_at')
    ordering = ('-id',)
    search_fields = ['name']
    serializer_class = VendorSerializer

    def get_serializer_class(self):

        if self.action in ['list']:

            return VendorListSerializer

        return VendorSerializer
