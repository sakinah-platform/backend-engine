from django.db import models
from django_softdelete.models import SoftDeleteModel

from master_data.models.vendor import Vendor


class VendorPackage(SoftDeleteModel):

    name = models.CharField(max_length=100,
                            unique=True,
                            blank=False,
                            null=False)
    vendor = models.ForeignKey(Vendor,
                               related_name='packages',
                               on_delete=models.PROTECT,
                               blank=False)
    price = models.PositiveIntegerField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = "vendor_package"
        get_latest_by = ["-created_at"]

    def __str__(self):
        return self.name
