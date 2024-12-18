
from rest_framework import routers
from master_data.api_handlers.vendor_category_handler import VendorCategoryViewSet
from master_data.api_handlers.vendor_handler import VendorViewSet
from master_data.api_handlers.city_handler import CityViewSet


# mapping urls
class MasterDataRouter:
    def __init__(self):
        self.router = routers.DefaultRouter()

    def result(self):

        self.router.register(r'vendor_category', VendorCategoryViewSet)
        self.router.register(r'city', CityViewSet)
        self.router.register(r'vendors', VendorViewSet)

        return self.router.urls
