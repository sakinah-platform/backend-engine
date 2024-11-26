from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import mixins, filters, serializers
from rest_framework.viewsets import GenericViewSet

from backend.system_utility.custom_search_utility import CustomSearchFilter
from backend.system_utility.pagination_utility import FiftyResultsPagination
from backend.system_utility.settings_utility import string_for_datetime, DEFAULT_CACHE_TIME
from master_data.business_logic.logic_vendor_category import get_vendor_categories
from master_data.models import VendorCategory

class VendorCategoryListSerializer(serializers.ModelSerializer):

    name = serializers.CharField(read_only=True)
    icon = serializers.FileField(use_url=True, read_only=True)

    class Meta:
        model = VendorCategory
        fields = ('id', 'name', 'icon')

class VendorCategoryReadSerializer(VendorCategoryListSerializer):

    description = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, format=string_for_datetime())

    class Meta:
        model = VendorCategory
        fields = ('id', 'name', 'description', 'icon')

@method_decorator(cache_page(DEFAULT_CACHE_TIME), name='list')
class VendorCategoryViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):

    queryset = get_vendor_categories()
    pagination_class = FiftyResultsPagination
    filter_backends = [filters.OrderingFilter, CustomSearchFilter]
    ordering_fields = ('id', 'name', 'created_at')
    ordering = ('-id',)
    search_fields = ['name', 'description']

    def get_serializer_class(self):

        if self.action in ['list']:

            return VendorCategoryListSerializer

        return VendorCategoryReadSerializer


