from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import mixins, filters
from rest_framework.viewsets import GenericViewSet

from backend.system_utility.custom_search_utility import CustomSearchFilter
from backend.system_utility.settings_utility import DEFAULT_CACHE_TIME

from master_data.models.vendor import Vendor
from master_data.serializers.vendor_serializer import VendorSerializer


class VendorViewSet(mixins.RetrieveModelMixin, GenericViewSet):

    queryset = Vendor.objects.all()
    filter_backends = [filters.OrderingFilter, CustomSearchFilter]
    ordering_fields = ('id', 'name', 'created_at')
    ordering = ('-id',)
    search_fields = ['name', 'category']
    serializer_class = VendorSerializer
