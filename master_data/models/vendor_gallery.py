from django.db import models
from django.core.validators import FileExtensionValidator
from os import path

from master_data.utility.media_utility import rel_path, ALLOWED_IMAGE_EXTENSIONS
from master_data.models.base import BaseModelManager
from master_data.models.vendor import Vendor


def vendor_galleries(_, curr_file):
    filename, ext = path.splitext(curr_file)

    return rel_path('vendor_galleries', filename, ext)


class VendorGallery(models.Model):

    image = models.ImageField(upload_to=vendor_galleries,
                              validators=[FileExtensionValidator(allowed_extensions=ALLOWED_IMAGE_EXTENSIONS)],
                              null=False,
                              blank=False)
    vendor = models.ForeignKey(Vendor,
                               related_name='galleries',
                               on_delete=models.PROTECT,
                               blank=False)
    deleted_flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BaseModelManager()

    class Meta:

        db_table = "master_vendor_gallery"
        get_latest_by = ["-created_at"]

    def __str__(self):
        return path.split(self.image.url)[1]
