from django.db.models import QuerySet

from master_data.models import VendorCategory


def get_vendor_categories() -> QuerySet[VendorCategory]:


    return VendorCategory.objects.filter(deleted_flag=False)
