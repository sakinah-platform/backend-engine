from django.db.models import QuerySet

from master_data.models.vendor_category import VendorCategory


def get_vendor_categories() -> QuerySet[VendorCategory]:

    return VendorCategory.objects.filter(deleted_flag=False)
