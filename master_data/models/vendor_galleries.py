from django.db import models

from master_data.utility.media_utility import vendor_galleries
from master_data.models.vendor import Vendor

import os


class BaseModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_flag=False)


class VendorGallery(models.Model):

    image = models.ImageField(upload_to=vendor_galleries,
                              null=False,
                              blank=False)
    vendor = models.ForeignKey(Vendor,
                               on_delete=models.PROTECT,
                               blank=True)
    deleted_flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BaseModelManager()

    class Meta:

        db_table = "master_vendor_gallery"
        get_latest_by = ["-created_at"]

    def __str__(self):
        return os.path.split(self.image.url)[1]
