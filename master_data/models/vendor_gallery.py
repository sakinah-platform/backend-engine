import uuid

from django.db import models
from django.core.validators import FileExtensionValidator
from django_softdelete.models import SoftDeleteModel
from os import path

from master_data.utility.media_utility import rel_path, ALLOWED_IMAGE_EXTENSIONS
from master_data.models.vendor import Vendor


def vendor_galleries(_, curr_file):
    filename, ext = path.splitext(curr_file)

    return rel_path('vendor_galleries', filename, ext)


class VendorGallery(SoftDeleteModel):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    image = models.ImageField(upload_to=vendor_galleries,
                              validators=[FileExtensionValidator(allowed_extensions=ALLOWED_IMAGE_EXTENSIONS)],
                              null=False,
                              blank=False)
    vendor = models.ForeignKey(Vendor,
                               related_name='galleries',
                               on_delete=models.PROTECT,
                               blank=False)
    vendor_old_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = "vendor_gallery"
        get_latest_by = ["-created_at"]

    def __str__(self):
        return path.split(self.image.url)[1]
