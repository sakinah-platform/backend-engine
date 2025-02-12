from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import mixins, filters
from rest_framework.viewsets import GenericViewSet

from backend.system_utility.custom_search_utility import CustomSearchFilter
from backend.system_utility.pagination_utility import FiftyResultsPagination
from backend.system_utility.settings_utility import DEFAULT_CACHE_TIME
from master_data.models.city import City
from master_data.serializers.city_serializer import CityListSerializer, CityReadSerializer


@method_decorator(cache_page(DEFAULT_CACHE_TIME), name='list')
class CityViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):

    queryset = City.objects.all()
    pagination_class = FiftyResultsPagination
    filter_backends = [filters.OrderingFilter, CustomSearchFilter]
    ordering_fields = ('id', 'name', 'created_at')
    ordering = ('-id',)
    search_fields = ['name', 'description']

    def get_serializer_class(self):

        if self.action in ['list']:

            return CityListSerializer

        return CityReadSerializer
