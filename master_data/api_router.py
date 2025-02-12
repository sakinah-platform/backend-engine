
from rest_framework_nested import routers
from master_data.api_handlers.vendor_category_handler import VendorCategoryViewSet
from master_data.api_handlers.vendor_handler import VendorViewSet
from master_data.api_handlers.city_handler import CityViewSet
from master_data.api_handlers.vendor_package_handler import VendorPackageViewSet


# mapping urls
class MasterDataRouter:
    def __init__(self):
        self.router = routers.DefaultRouter()

    def result(self):

        self.router.register(r'vendor_category', VendorCategoryViewSet)
        self.router.register(r'city', CityViewSet)
        self.router.register(r'vendors', VendorViewSet)

        vendors_router = routers.NestedSimpleRouter(self.router, r'vendors', lookup='vendor')
        vendors_router.register(r'packages', VendorPackageViewSet, basename='vendorpackage')

        return self.router.urls + vendors_router.urls
