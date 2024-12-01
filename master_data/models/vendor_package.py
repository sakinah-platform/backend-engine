from django.db import models

from master_data.models.vendor import Vendor
from master_data.models.base import BaseModelManager


class VendorPackage(models.Model):

    name = models.CharField(max_length=100,
                            unique=True,
                            blank=False,
                            null=False)
    vendor = models.ForeignKey(Vendor,
                               on_delete=models.PROTECT,
                               blank=True)
    price = models.PositiveIntegerField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    deleted_flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BaseModelManager()

    class Meta:

        db_table = "master_vendor_packages"
        get_latest_by = ["-created_at"]

    def __str__(self):
        return self.name
